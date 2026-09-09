"""Start ALFRED; importing this file has no side effects."""
if __name__ == "__main__":
    from assistant_core.app import launch
    raise SystemExit(launch("alfred", __file__))
