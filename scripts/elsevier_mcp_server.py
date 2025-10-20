#!/usr/bin/env python3
"""
Elsevier API MCP Server
文献検索のためのModel Context Protocol サーバー
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional, Dict, Any, List

# 環境変数から設定を取得
ELSEVIER_API_KEY = os.environ.get("ELSEVIER_API_KEY", "")
ELSEVIER_INSTTOKEN = os.environ.get("ELSEVIER_INSTTOKEN", "")

# Elsevier API エンドポイント
SCOPUS_SEARCH_URL = "https://api.elsevier.com/content/search/scopus"
SCIENCEDIRECT_SEARCH_URL = "https://api.elsevier.com/content/search/sciencedirect"
ABSTRACT_RETRIEVAL_URL = "https://api.elsevier.com/content/abstract/scopus_id/"


class ElsevierMCPServer:
    """Elsevier API用のMCPサーバー"""
    
    def __init__(self, api_key: str, inst_token: Optional[str] = None):
        self.api_key = api_key
        self.inst_token = inst_token
        self.headers = {
            "X-ELS-APIKey": self.api_key,
            "Accept": "application/json"
        }
        if self.inst_token:
            self.headers["X-ELS-Insttoken"] = self.inst_token
    
    def search_scopus(self, query: str, count: int = 10, start: int = 0) -> Dict[str, Any]:
        """
        Scopusデータベースを検索
        
        Args:
            query: 検索クエリ（例: "EEG AND brain-computer interface"）
            count: 取得する結果数（最大25）
            start: 開始位置
            
        Returns:
            検索結果の辞書
        """
        params = {
            "query": query,
            "count": str(min(count, 25)),
            "start": str(start),
            "sort": "-citedby-count"  # 引用数の多い順
        }
        
        try:
            url = f"{SCOPUS_SEARCH_URL}?{urllib.parse.urlencode(params)}"
            req = urllib.request.Request(url, headers=self.headers)
            
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                return json.loads(data.decode('utf-8'))
        except urllib.error.URLError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}
    
    def search_sciencedirect(self, query: str, count: int = 10, start: int = 0) -> Dict[str, Any]:
        """
        ScienceDirectデータベースを検索
        
        Args:
            query: 検索クエリ
            count: 取得する結果数（最大25）
            start: 開始位置
            
        Returns:
            検索結果の辞書
        """
        params = {
            "query": query,
            "count": str(min(count, 25)),
            "start": str(start)
        }
        
        try:
            url = f"{SCIENCEDIRECT_SEARCH_URL}?{urllib.parse.urlencode(params)}"
            req = urllib.request.Request(url, headers=self.headers)
            
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                return json.loads(data.decode('utf-8'))
        except urllib.error.URLError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}
    
    def get_abstract(self, scopus_id: str) -> Dict[str, Any]:
        """
        Scopus IDから論文の抄録を取得
        
        Args:
            scopus_id: Scopus ID（例: "SCOPUS_ID:85012345678"）
            
        Returns:
            抄録情報の辞書
        """
        url = f"{ABSTRACT_RETRIEVAL_URL}{scopus_id}"
        
        try:
            req = urllib.request.Request(url, headers=self.headers)
            
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                return json.loads(data.decode('utf-8'))
        except urllib.error.URLError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}
    
    def format_scopus_results(self, results: Dict[str, Any]) -> str:
        """Scopus検索結果を読みやすい形式にフォーマット"""
        if "error" in results:
            return f"Error: {results['error']}"
        
        if "search-results" not in results:
            return "No results found."
        
        search_results = results["search-results"]
        total_results = search_results.get("opensearch:totalResults", "0")
        entries = search_results.get("entry", [])
        
        output = [f"Total results: {total_results}\n"]
        
        for i, entry in enumerate(entries, 1):
            title = entry.get("dc:title", "No title")
            authors = entry.get("dc:creator", "Unknown")
            pub_name = entry.get("prism:publicationName", "Unknown journal")
            pub_date = entry.get("prism:coverDate", "Unknown date")
            cited_by = entry.get("citedby-count", "0")
            doi = entry.get("prism:doi", "No DOI")
            scopus_id = entry.get("dc:identifier", "").replace("SCOPUS_ID:", "")
            
            output.append(f"{i}. {title}")
            output.append(f"   Authors: {authors}")
            output.append(f"   Journal: {pub_name} ({pub_date})")
            output.append(f"   Cited by: {cited_by}")
            output.append(f"   DOI: {doi}")
            output.append(f"   Scopus ID: {scopus_id}")
            output.append("")
        
        return "\n".join(output)
    
    def handle_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """MCPコマンドを処理"""
        cmd_type = command.get("type")
        params = command.get("params", {})
        
        if cmd_type == "search_scopus":
            query = params.get("query", "")
            count = params.get("count", 10)
            results = self.search_scopus(query, count)
            formatted = self.format_scopus_results(results)
            return {
                "type": "response",
                "data": formatted,
                "raw": results
            }
        
        elif cmd_type == "search_sciencedirect":
            query = params.get("query", "")
            count = params.get("count", 10)
            results = self.search_sciencedirect(query, count)
            return {
                "type": "response",
                "data": results
            }
        
        elif cmd_type == "get_abstract":
            scopus_id = params.get("scopus_id", "")
            results = self.get_abstract(scopus_id)
            return {
                "type": "response",
                "data": results
            }
        
        else:
            return {
                "type": "error",
                "message": f"Unknown command type: {cmd_type}"
            }


def main():
    """メイン関数"""
    if not ELSEVIER_API_KEY:
        print("ERROR: ELSEVIER_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)
    
    server = ElsevierMCPServer(ELSEVIER_API_KEY, ELSEVIER_INSTTOKEN)
    
    # コマンドライン引数から検索実行
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "search":
            if len(sys.argv) < 3:
                print("Usage: elsevier_mcp_server.py search <query>", file=sys.stderr)
                sys.exit(1)
            
            query = " ".join(sys.argv[2:])
            print(f"Searching Scopus for: {query}\n")
            results = server.search_scopus(query, count=10)
            print(server.format_scopus_results(results))
        
        elif command == "abstract":
            if len(sys.argv) < 3:
                print("Usage: elsevier_mcp_server.py abstract <scopus_id>", file=sys.stderr)
                sys.exit(1)
            
            scopus_id = sys.argv[2]
            results = server.get_abstract(scopus_id)
            print(json.dumps(results, indent=2))
        
        else:
            print(f"Unknown command: {command}", file=sys.stderr)
            print("Available commands: search, abstract", file=sys.stderr)
            sys.exit(1)
    
    else:
        # 対話モード（JSON-RPC風）
        print("Elsevier MCP Server started. Enter commands as JSON.", file=sys.stderr)
        for line in sys.stdin:
            try:
                command = json.loads(line)
                response = server.handle_command(command)
                print(json.dumps(response))
                sys.stdout.flush()
            except json.JSONDecodeError as e:
                error_response = {
                    "type": "error",
                    "message": f"Invalid JSON: {e}"
                }
                print(json.dumps(error_response))
                sys.stdout.flush()


if __name__ == "__main__":
    main()

