# RESULTADO DO BENCHMARK: ASSISTENTE DE FATURAMENTO MÉDICO

Este arquivo documenta os resultados gerados por um modelo de IA para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico

**Prompt:** `Preciso de ajuda com faturamento médico.`

**Resultado:**

Com certeza. O faturamento médico é uma área complexa. Para que eu possa ajudar, preciso entender melhor sua necessidade. Você poderia me dizer com o que exatamente precisa de ajuda? Por exemplo:

1.  **Você precisa encontrar um código específico** para um procedimento ou consulta (ex: TUSS, CBHPM)?
2.  **Você tem dúvidas sobre como preencher uma guia** de convênio?
3.  **Você está lidando com uma glosa** (recusa de pagamento) e precisa de orientação?
4.  **Você busca informações gerais** sobre as regras de um convênio específico?

**AVISO IMPORTANTE:** Eu sou uma ferramenta de IA e não um especialista em faturamento médico. Minhas respostas são baseadas em informações públicas e devem ser usadas apenas como orientação. Sempre valide as informações com as tabelas oficiais e as regras da operadora de saúde em questão.

---

## 2. Resposta ao Prompt Estruturado (JSON)

**Prompt:**
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

**Resultado:**

### Código TUSS para Consulta com Cardiologista

**Código TUSS:** `10101012`

**Descrição:** Este código refere-se a uma **"Consulta em consultório (no horário normal ou preestabelecido)"**. Ele é o código padrão utilizado para a primeira consulta com um médico especialista, como um cardiologista.

**Observações e Requisitos:**

*   **Especialidade:** Ao preencher a guia de faturamento, o campo da especialidade do médico executante deve ser preenchido como "Cardiologia".
*   **Autorização Prévia:** A necessidade de autorização prévia para consultas pode variar significativamente entre as diferentes operadoras de saúde e os planos contratados. É **fundamental** verificar o manual do convênio ou contatar diretamente a operadora para confirmar se a autorização é necessária antes do atendimento.
*   **Consulta de Retorno:** Para consultas de retorno, dentro de um prazo definido pela operadora, geralmente se utiliza um código diferente (ex: 10101039 - Retorno em Consultório), que pode ou não ser remunerado.

**AVISO:** Esta informação é baseada em interpretações da tabela TUSS e serve como orientação. **Não deve ser considerada aconselhamento financeiro ou regulatório.** As regras de faturamento e a necessidade de autorização são determinadas por cada operadora de saúde. Sempre consulte a documentação oficial da ANS e da operadora.

---

## 3. Resposta ao Prompt Estruturado (KERNEL)

**Prompt:**
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

**Resultado:**

### Identificação de Código TUSS: Consulta em Cardiologia

#### **Código do Procedimento**
`10101012`

#### **Descrição do Procedimento**
O código corresponde a **"Consulta em consultório"**. É o código genérico para uma primeira consulta eletiva com qualquer especialista, incluindo Cardiologia.

#### **Observações Relevantes**
1.  **Validação com a Operadora:** As regras de faturamento, incluindo a necessidade de autorização prévia, são específicas de cada operadora de saúde. É imprescindível consultar as normas do convênio antes de enviar o faturamento.
2.  **Diferenciação de Retorno:** Este código é para a primeira consulta. Consultas de retorno para apresentação de exames ou acompanhamento podem exigir um código diferente, conforme as regras da operadora.
3.  **Versão da Tabela:** Certifique-se de que o sistema de faturamento da clínica está utilizando a versão mais recente da tabela TUSS, conforme determinado pela ANS (Agência Nacional de Saúde Suplementar).

---
**AVISO LEGAL**

Esta resposta é uma referência baseada na tabela TUSS e não constitui aconselhamento regulatório ou financeiro. A responsabilidade de verificar e aplicar corretamente os códigos e regras de faturamento é do prestador de serviço, de acordo com os contratos estabelecidos com cada operadora de saúde.
---
