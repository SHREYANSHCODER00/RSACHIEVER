kivy==2.0.0
kivymd==0.104.1
# Add any other dependencies your app may need
name: Build APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: RSACHIEVER
        uses: actions/checkout@v2

      - name: Set Up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install Dependencies
        run: |
          pip install buildozer
          buildozer init
          buildozer -v android debug

      - name: RSACHIEVER
        uses: actions/upload-artifact@v2
        with:
          name: RSACHIEVER
          path: bin/
steps:
  - name: Checkout Repository
    uses: actions/checkout@v2

  - name: Set Up Python
    uses: actions/setup-python@v2
    with:
      python-version: 3.8

  - name: Install Dependencies
    run: |
      pip install buildozer
      buildozer init
      buildozer -v android debug

  - name: RSACHIEVER
    uses: actions/upload-artifact@v2
    with:
      name: RSACHIEVER
      path: bin/
