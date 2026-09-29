#!/usr/bin/env python3
from pathlib import Path
from playwright.sync_api import sync_playwright

LANDING="https://www.bls.gov/tus/data/datafiles-0324.htm"
FILES=[
    "atusresp-0324.zip",
    "atusrost-0324.zip",
    "atusact-0324.zip",
    "atussum-0324.zip",
    "atuswho-0324.zip",
    "atuscps-0324.zip",
]

out=Path("data/raw/atus/2003-2024")
out.mkdir(parents=True,exist_ok=True)

with sync_playwright() as p:
    browser=p.chromium.launch(
        headless=False,
        executable_path="/usr/bin/google-chrome",
        args=["--no-sandbox","--disable-dev-shm-usage"],
    )
    ctx=browser.new_context(
        accept_downloads=True,
        locale="en-US",
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    )
    page=ctx.new_page()
    page.goto(LANDING, wait_until="domcontentloaded", timeout=120000)
    for fname in FILES:
        target=out/fname
        if target.exists() and target.stat().st_size>0:
            print("[skip]",fname)
            continue
        sel=f'a[href$="{fname}"]'
        locator=page.locator(sel)
        if locator.count()!=1:
            raise RuntimeError(f"Expected one link for {fname}, found {locator.count()}")
        print("[browser download]",fname)
        with page.expect_download(timeout=180000) as info:
            locator.click()
        dl=info.value
        dl.save_as(str(target))
        if not target.exists() or target.stat().st_size==0:
            raise RuntimeError(f"Empty download: {fname}")
        print(fname,target.stat().st_size)
    browser.close()
