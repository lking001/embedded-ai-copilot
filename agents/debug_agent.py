class DebugAgent:
    def analyze(self, issue):
        if "DMA" in issue and "中断" in issue:
            return """
可能原因：
1. NVIC 未使能
2. DMA 中断标志未清除
3. FIFO 阈值配置错误

建议：
- 检查 HAL_NVIC_EnableIRQ
- 检查 DMA_SxCR 配置
"""
        return "暂未识别问题"
