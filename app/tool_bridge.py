from mcp.client.session import MCPClient
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

class ToolBridge:
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url

    async def read_file(self, path: str) -> str:
        logging.info(f"Requesting file from MCP: {path}")
        async with MCPClient(self.server_url) as client:
            return await client.get_resource(f"file://{path}")

    async def list_files(self, directory: str) -> list[str]:
        logging.info(f"Requesting file list from MCP for: {directory}")
        async with MCPClient(self.server_url) as client:
            return await client.call_tool("list_files", {"directory": directory})

    async def get_capabilities(self) -> dict:
        logging.info("Requesting capabilities from MCP")
        async with MCPClient(self.server_url) as client:
            return await client.call_tool("get_capabilities", {})
