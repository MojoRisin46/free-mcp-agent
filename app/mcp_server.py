from mcp.server.fastmcp import FastMCP
import os
import logging

logging.basicConfig(level=logging.INFO)
mcp = FastMCP("MotoGPTools")

# tools, that are currently not yet used! In the future I want to implement them.

@mcp.resource("file://{path}")
def read_file(path: str) -> str:
    logging.info(f"Reading file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

@mcp.tool()
def list_files(directory: str) -> list[str]:
    logging.info(f"Listing files in: {directory}")
    return os.listdir(directory)

@mcp.tool()
def get_capabilities() -> dict:
    logging.info("Providing tool and resource capabilities")
    return {
        "tools": ["read_file", "list_files"],
        "resources": ["file://{path}"]
    }


# actual running of MCP server, super simple with the mcp module

if __name__ == "__main__":
    logging.info("Starting MCP server")
    mcp.run()
