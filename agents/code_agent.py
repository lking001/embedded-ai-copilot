class CodeAgent:
    def generate_dma_init(self):
        return """
void DMA_Config(void)
{
    // DMA 初始化示例
    hdma.Init.Direction = DMA_MEMORY_TO_PERIPH;
    hdma.Init.MemDataAlignment = DMA_MDATAALIGN_HALFWORD;
    hdma.Init.PeriphDataAlignment = DMA_PDATAALIGN_HALFWORD;
}
"""
