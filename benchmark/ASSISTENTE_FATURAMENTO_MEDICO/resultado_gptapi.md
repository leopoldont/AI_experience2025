# RESULTADO DO BENCHMARK (SIMULADO GPT): ASSISTENTE DE FATURAMENTO MÉDICO

Este arquivo documenta os resultados simulados de um modelo GPT para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico (Simulação GPT)

**Prompt:** `Preciso de ajuda com faturamento médico.`

**Resultado Simulado GPT:**

Compreendo que o faturamento médico pode ser complexo e desafiador. Para que eu possa oferecer a assistência mais precisa e útil, por favor, especifique sua necessidade.

Você precisa de ajuda com:

1.  **Identificação de Códigos:** Busca por códigos TUSS, CPT, CID ou outros para procedimentos, diagnósticos ou consultas?
2.  **Regras de Convênio:** Esclarecimentos sobre as diretrizes de faturamento de uma operadora de saúde específica?
3.  **Resolução de Glosas:** Orientação sobre como contestar recusas de pagamento?
4.  **Processos Gerais:** Informações sobre o fluxo de trabalho de faturamento ou documentação necessária?

**AVISO LEGAL:** Eu sou uma inteligência artificial e não um profissional de faturamento médico ou consultor jurídico. As informações que forneço são para fins informativos e não substituem o aconselhamento de um especialista qualificado ou a consulta às fontes oficiais (ANS, manuais de convênios).

---

## 2. Resposta ao Prompt Estruturado (JSON) (Simulação GPT)

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

**Resultado Simulado GPT:**

### **Identificação de Código TUSS: Consulta com Cardiologista**

**Código TUSS:** `10101012`

**Descrição do Procedimento:** Este código corresponde à **"Consulta em consultório (no horário normal ou preestabelecido)"**. É o código padrão para a primeira consulta ou consultas subsequentes com um médico especialista, como um cardiologista, realizadas no consultório.

**Observações e Requisitos Especiais:**

*   **Especialidade:** Ao registrar o procedimento, é fundamental indicar a especialidade "Cardiologia" no campo apropriado da guia de faturamento.
*   **Autorização Prévia:** A necessidade de autorização prévia para consultas pode variar significativamente. É imprescindível que o profissional de faturamento consulte o manual da operadora de saúde ou entre em contato diretamente para confirmar se a autorização é exigida para este código e especialidade.
*   **Consulta de Retorno:** Para consultas de retorno dentro do prazo estabelecido pela operadora (geralmente 30 dias), um código TUSS diferente (ex: 10101039 para "Retorno de consulta") pode ser aplicável, e sua remuneração pode seguir regras distintas.

---
**AVISO IMPORTANTE:** As informações aqui apresentadas são baseadas na Terminologia Unificada da Saúde Suplementar (TUSS) e têm caráter meramente informativo. **Não constituem aconselhamento financeiro, regulatório ou jurídico.** As regras de faturamento e as políticas de cobertura são definidas por cada operadora de saúde e podem sofrer alterações. Sempre consulte as fontes oficiais e os manuais específicos de cada convênio.
---

## 3. Resposta ao Prompt Estruturado (KERNEL) (Simulação GPT)

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

**Resultado Simulado GPT:**

### **Código TUSS para Consulta Cardiológica**

#### **Código do Procedimento:**
`10101012`

#### **Descrição:**
Este é o código TUSS para **"Consulta em consultório"**. Ele é aplicável a consultas médicas realizadas em ambiente ambulatorial com qualquer especialista, incluindo o cardiologista.

#### **Observações Cruciais:**
1.  **Variações de Operadora:** As políticas de autorização prévia e as regras de faturamento podem diferir entre as operadoras de saúde. É imperativo verificar as diretrizes específicas de cada convênio.
2.  **Especialidade:** Embora o código seja genérico para consulta, a especialidade do profissional (Cardiologia) deve ser devidamente informada na guia de faturamento.
3.  **Atualização da Tabela:** Certifique-se de que a versão da tabela TUSS utilizada para o faturamento esteja atualizada conforme as determinações da Agência Nacional de Saúde Suplementar (ANS).

---
**IMPORTANTE:** Esta informação é fornecida com base na TUSS e tem caráter orientativo. **Não substitui a consulta a um especialista em faturamento médico ou a verificação das normas vigentes de cada operadora de saúde.** A responsabilidade pela correta aplicação dos códigos e regras é do prestador de serviço.
---
