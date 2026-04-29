from rag.vector_store import VectorStore
from rag.loader import load_docs
from agents.doc_agent import DocAgent
from agents.code_agent import CodeAgent
from agents.debug_agent import DebugAgent

def main():
    # 初始化 RAG
    docs = load_docs("data/sample_rm.txt")
    store = VectorStore()
    store.add(docs)

    # 初始化 Agents
    doc_agent = DocAgent(store)
    code_agent = CodeAgent()
    debug_agent = DebugAgent()

    print("=== 文档查询 ===")
    print(doc_agent.query("DMA FIFO"))

    print("\n=== 代码生成 ===")
    print(code_agent.generate_dma_init())

    print("\n=== 问题分析 ===")
    print(debug_agent.analyze("DMA 无中断"))

if __name__ == "__main__":
    main()
