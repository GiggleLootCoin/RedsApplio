import os
from pathlib import Path

import spaces

os.environ.setdefault("URVC_ACCELERATOR", "cuda")

# Patch the upstream web source before importing it so the title and colors
# are ours while the underlying Ultimate RVC functionality remains upstream.
main_path = Path("/home/user/.local/lib/python3.12/site-packages/ultimate_rvc/web/main.py")
if not main_path.exists():
    candidates = list(Path("/usr/local/lib/python3.12/site-packages").glob("ultimate_rvc/web/main.py"))
    candidates += list(Path("/opt/pyvenv/lib/python3.12/site-packages").glob("ultimate_rvc/web/main.py"))
    if candidates:
        main_path = candidates[0]

if main_path.exists():
    source = main_path.read_text(encoding="utf-8")
    source = source.replace('Ultimate RVC 💙', "Red's Ultimate RVC ❤️")
    red_css = r'''
    body, .gradio-container { background: #050505 !important; color: #f4f4f4 !important; }
    h1, h2, h3, h4, label { color: #ff2020 !important; }
    button { background: #a80000 !important; color: #ffffff !important; border-color: #ff2020 !important; }
    button:hover { background: #df0000 !important; }
    input, textarea, .block, .panel, .tabs, .tabitem {
        background: #0a0a0a !important; color: #f4f4f4 !important; border-color: #401010 !important;
    }
    input:focus, textarea:focus { border-color: #ff2020 !important; }
    .tab-nav button.selected, .tab-nav button[aria-selected="true"] {
        color: #ff2020 !important; border-color: #ff2020 !important;
    }
    footer { display: none !important; }
    '''
    marker = '    css = """'
    if marker in source and red_css not in source:
        start = source.index(marker)
        end = source.index('"""', start + len(marker))
        source = source[:end] + red_css + source[end:]
    main_path.write_text(source, encoding="utf-8")

# Ultimate RVC's UI already routes these operations through its GPU
# concurrency group. ZeroGPU additionally needs @spaces.GPU to allocate
# the actual shared GPU for the work.
from ultimate_rvc.core.generate import common as generate_common
from ultimate_rvc.core.generate import song_cover

def _gpu(module, name, duration=120):
    fn = getattr(module, name)
    setattr(module, name, spaces.GPU(duration=duration)(fn))

for _name in ("convert",):
    _gpu(generate_common, _name)

for _name in (
    "run_pipeline",
    "separate_audio",
    "postprocess",
    "pitch_shift",
    "mix_song",
):
    _gpu(song_cover, _name)

from ultimate_rvc.web import main

if __name__ == "__main__":
    main.app.queue(default_concurrency_limit=1)
    main.app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        ssr_mode=False,
    )
