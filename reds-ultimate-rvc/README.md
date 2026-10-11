---
title: Red's Ultimate RVC ❤️
emoji: ❤️
colorFrom: red
colorTo: gray
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
python_version: "3.12.12"
startup_duration_timeout: 1h
pinned: false
license: mit
short_description: Red's black-and-red Ultimate RVC studio
---

# Red's Ultimate RVC ❤️

A ZeroGPU-ready Gradio build of Ultimate RVC 0.6.0, customized for LittleRedBigSmile.

## Main workflow

- Upload a song.
- Separate vocals and instrumental.
- Choose an RVC voice model.
- Convert the vocals.
- Mix the converted vocals back with the music.
- Download the finished cover.

The app also retains Ultimate RVC's model/audio/settings areas.

## ZeroGPU

This build wraps the heavy Ultimate RVC song-processing functions with `@spaces.GPU` so a free Hugging Face ZeroGPU Space can request GPU compute only while processing. Hugging Face currently documents ZeroGPU as the free hosting route for eligible personal Gradio Spaces. citeturn3search0

Ultimate RVC 0.6.0 requires Python 3.12–3.13, so this build intentionally does not use the broken Python 3.10 runtime that caused the previous build failure.

## Important free-tier limit

ZeroGPU has a daily GPU quota and per-call duration limits. Long songs may need to be processed through the multi-step workflow rather than a single one-click call. citeturn4search0

Source project: JackismyShephard/ultimate-rvc.
