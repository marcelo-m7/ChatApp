import sysif sys.platform == "emscripten": # check if run in Pyodide environment    import micropip    await micropip.install("regex")

