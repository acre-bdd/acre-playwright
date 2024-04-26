from radish import world

from acre.lib import artifacts, settings, log


class _Browser:
    def start(self):
        world.browser = world.playwright.chromium.launch(headless=settings.playwright.browser.headless)
        world.context = world.browser.new_context(
            record_video_dir=artifacts.directory,
            viewport={"width": 600, "height": 800})
        world.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        world.page = None

    def stop(self):
        world.context.tracing.stop(path=artifacts.file(".trace.zip"))
        world.browser.close()
        world.browser = None

    def open(self, url):
        if not world.page:
            world.page = world.context.new_page()
        log.note(f"opening url '{url}'")
        world.page.goto(url)

    @property
    def is_running():
        return world.browser is not None


Browser = _Browser()
