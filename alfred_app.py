"""Start ALFRED; importing this file has no side effects."""
# Original publisher: lkghost327-afk — https://github.com/lkghost327-afk/ALFRED
if __name__ == "__main__":
    from assistant_core.app import launch
    raise SystemExit(launch("alfred", __file__))
