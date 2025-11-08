# PROMPTS PARA ASSISTENTE DE FATURAMENTO MÉDICO

---

## 1. Prompt Genérico

Preciso de ajuda com faturamento médico.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "identificar_codigo_de_procedimento_medico",
  "context": {
    "background": "Um profissional de faturamento de uma clínica precisa encontrar o código correto para um procedimento na tabela TUSS.",
    "user_goal": "Encontrar o código TUSS para 'Consulta com especialista em cardiologia'."
  },
  "instructions": {
    "steps": [
      "Buscar na tabela TUSS (Terminologia Unificada da Saúde Suplementar) o código correspondente a uma consulta com um cardiologista.",
      "Fornecer o código exato do procedimento.",
      "Descrever brevemente o que o código representa.",
      "Indicar se há alguma observação ou requisito especial para a utilização desse código (ex: necessidade de autorização prévia)."
    ],
    "output_format": "Texto claro com o código em destaque, seguido pela descrição e observações."
  },
  "constraints": [
    "A informação deve ser baseada na versão mais recente da tabela TUSS disponível.",
    "**NÃO DEVE SER CONSIDERADO ACONSELHAMENTO FINANCEIRO OU REGULATÓRIO.**",
    "Incluir um aviso de que as regras de faturamento podem variar entre operadoras de saúde."
  ],
  "user_input": "Qual o código TUSS para consulta com cardiologista?"
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Encontrar o código TUSS para uma consulta com cardiologista.
- **E (Easy to verify):** O resultado deve apresentar um código, sua descrição e possíveis observações.
- **R (Reproducible results):** O código TUSS para um procedimento específico é padronizado (dentro de uma mesma versão da tabela).
- **N (Narrow scope):** A tarefa foca em encontrar um único código de procedimento.
- **E (Explicit constraints):** Usar a tabela TUSS como referência. Incluir aviso sobre variações entre operadoras.
- **L (Logical structure):**

    1.  **Task:** Identificar o código TUSS para 'consulta com especialista em cardiologia'.
    2.  **Input:** Necessidade de encontrar um código de procedimento médico.
    3.  **Constraints:** A resposta deve ser baseada na tabela TUSS. Incluir aviso legal.
    4.  **Output:** Código do procedimento, sua descrição e observações relevantes.
    5.  **Verify:** Confirmar se o código fornecido corresponde ao procedimento solicitado e se os avisos foram incluídos.
