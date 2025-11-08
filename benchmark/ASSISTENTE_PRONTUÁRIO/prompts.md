# PROMPTS PARA ASSISTENTE DE PRONTUÁRIO ELETRÔNICO

---

## 1. Prompt Genérico

Resuma este prontuário.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "resumir_prontuario_paciente",
  "context": {
    "background": "Um médico precisa de um resumo rápido da história de um paciente antes de uma consulta.",
    "user_goal": "Extrair e estruturar as informações mais relevantes de um longo prontuário médico."
  },
  "instructions": {
    "steps": [
      "Identificar as informações demográficas básicas do paciente (Nome, Idade, Gênero).",
      "Listar as condições crônicas diagnosticadas (ex: Hipertensão, Diabetes).",
      "Listar as alergias conhecidas.",
      "Resumir as 3 últimas consultas, incluindo data, queixa principal e tratamento prescrito.",
      "Apresentar os resultados dos últimos 2 exames laboratoriais relevantes."
    ],
    "output_format": "Relatório estruturado com as seções: 'Dados do Paciente', 'Condições Crônicas', 'Alergias', 'Histórico Recente' e 'Exames'."
  },
  "constraints": [
    "A informação deve ser extraída de forma objetiva e sem interpretações.",
    "**A PRIVACIDADE E A CONFIDENCIALIDADE DOS DADOS DO PACIENTE SÃO PRIORIDADE MÁXIMA.**",
    "O resultado não deve conter informações de identificação pessoal além do primeiro nome (em um cenário real, usar identificadores anônimos)."
  ],
  "user_input": "[Conteúdo do prontuário médico aqui, com dados anonimizados]"
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Resumir as informações mais importantes de um prontuário de paciente.
- **E (Easy to verify):** O resumo deve conter dados demográficos, condições crônicas, alergias, resumo das 3 últimas consultas e 2 últimos exames.
- **R (Reproducible results):** A estrutura do resumo é padronizada.
- **N (Narrow scope):** A tarefa foca apenas em extrair e resumir os dados do prontuário fornecido.
- **E (Explicit constraints):** Manter a objetividade. Priorizar a privacidade. Não incluir dados sensíveis de identificação.
- **L (Logical structure):**

    1.  **Task:** Gerar um resumo estruturado de um prontuário eletrônico.
    2.  **Input:** Texto completo de um prontuário de paciente (anonimizado).
    3.  **Constraints:** Extração objetiva. **GARANTIR A CONFIDENCIALIDADE DOS DADOS.**
    4.  **Output:** Relatório estruturado com 5 seções claras sobre a saúde do paciente.
    5.  **Verify:** Checar se todas as 5 seções foram preenchidas corretamente com base no prontuário de entrada.
