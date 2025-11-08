# PROMPTS PARA ASSISTENTE FINANCEIRO MÉDICO

---

## 1. Prompt Genérico

Preciso de ajuda com as finanças da minha clínica.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "analisar_fluxo_de_caixa_de_clinica_medica",
  "context": {
    "background": "O gestor de uma clínica médica quer entender a saúde financeira do negócio.",
    "user_goal": "Analisar um relatório de fluxo de caixa simplificado e identificar pontos de melhoria."
  },
  "instructions": {
    "steps": [
      "Calcular o saldo operacional (Receitas - Despesas).",
      "Identificar os 3 maiores custos no período.",
      "Sugerir 2 ações práticas para otimizar as despesas ou aumentar as receitas com base nos dados fornecidos.",
      "Apresentar um resumo da análise em 3 frases."
    ],
    "output_format": "Relatório de análise estruturado com as seções: 'Saldo Operacional', 'Maiores Custos', 'Sugestões de Melhoria' e 'Resumo'."
  },
  "constraints": [
    "A análise deve ser baseada estritamente nos dados fornecidos.",
    "**NÃO DEVE SER CONSIDERADO ACONSELHAMENTO FINANCEIRO PROFISSIONAL.**",
    "Incluir um aviso para consultar um contador ou consultor financeiro qualificado."
  ],
  "user_input": "Relatório de Caixa (último mês): Receitas Totais: R$ 50.000. Despesas: Aluguel (R$ 10.000), Salários (R$ 25.000), Materiais (R$ 8.000), Marketing (R$ 2.000)."
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Analisar um fluxo de caixa simplificado de uma clínica médica.
- **E (Easy to verify):** O resultado deve conter o saldo operacional, os 3 maiores custos, 2 sugestões e um resumo.
- **R (Reproducible results):** Os cálculos são matemáticos e baseados nos dados de entrada.
- **N (Narrow scope):** A tarefa foca apenas na análise do fluxo de caixa fornecido.
- **E (Explicit constraints):** Análise restrita aos dados de entrada. Incluir aviso legal.
- **L (Logical structure):**

    1.  **Task:** Analisar o fluxo de caixa de uma clínica e sugerir melhorias.
    2.  **Input:** Receitas de R$ 50.000 e despesas com Aluguel (R$ 10.000), Salários (R$ 25.000), Materiais (R$ 8.000), Marketing (R$ 2.000).
    3.  **Constraints:** Não fazer suposições além dos dados. **DEVE** incluir um aviso para consultar um profissional.
    4.  **Output:** Relatório estruturado com Saldo, Maiores Custos, Sugestões e Resumo.
    5.  **Verify:** Checar se os cálculos estão corretos e se todas as seções do relatório foram geradas.
