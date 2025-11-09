# RESULTADO DO BENCHMARK (SIMULADO GPT): ASSISTENTE DE PRONTUÁRIO ELETRÔNICO

Este arquivo documenta os resultados simulados de um modelo GPT para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico (Simulação GPT)

**Prompt:** `Resuma este prontuário.`

**Resultado Simulado GPT:**

Compreendo a necessidade de resumir prontuários para otimizar o tempo e a compreensão. Por favor, cole o conteúdo do prontuário médico aqui para que eu possa processá-lo.

**ATENÇÃO MÁXIMA À PRIVACIDADE E CONFIDENCIALIDADE:**

É **IMPERATIVO** que você **ANONIMIZE COMPLETAMENTE** todas as informações de identificação pessoal do paciente antes de me fornecer o texto. Isso inclui, mas não se limita a:

*   Nome completo do paciente
*   Data de nascimento exata
*   Endereço, telefone, e-mail
*   Números de documentos (CPF, RG, prontuário)
*   Nomes de familiares ou outros identificadores únicos

Minha função é processar informações clínicas de forma objetiva. A responsabilidade pela anonimização e pela conformidade com as leis de proteção de dados (como a LGPD no Brasil) é inteiramente sua.

---

## 2. Resposta ao Prompt Estruturado (JSON) (Simulação GPT)

**Prompt:**
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

**Resultado Simulado GPT:**

**Nota:** O conteúdo do prontuário não foi fornecido no `user_input`. Para demonstrar a capacidade de extração e estruturação conforme o JSON, apresento um exemplo hipotético de resumo de prontuário anonimizado.

### **Resumo Estruturado do Prontuário do Paciente**

#### **Dados do Paciente**
*   **Nome:** Paciente "M. Silva" (anonimizado)
*   **Idade:** 55 anos
*   **Gênero:** Feminino

#### **Condições Crônicas Diagnosticadas**
*   Hipotiroidismo (desde 2018)
*   Enxaqueca Crônica (desde a adolescência)

#### **Alergias Conhecidas**
*   Dipirona (relata urticária)
*   Látex (relata dermatite de contato)

#### **Histórico Recente de Consultas (Últimas 3)**
1.  **Data: 20/06/2025**
    *   **Queixa Principal:** Crise de enxaqueca com aura visual.
    *   **Tratamento Prescrito:** Ajuste da medicação profilática (Topiramato 50mg 2x/dia). Orientação para repouso e hidratação.
2.  **Data: 15/03/2025**
    *   **Queixa Principal:** Acompanhamento de rotina do hipotiroidismo.
    *   **Tratamento Prescrito:** Mantida dose de Levotiroxina (75mcg/dia). Solicitado TSH e T4L.
3.  **Data: 05/12/2024**
    *   **Queixa Principal:** Dor articular difusa, principalmente em joelhos.
    *   **Tratamento Prescrito:** Analgésico e anti-inflamatório. Encaminhamento para reumatologista.

#### **Resultados de Exames Laboratoriais Relevantes (Últimos 2)**
1.  **TSH e T4 Livre (10/03/2025):**
    *   TSH: 2.8 mUI/L (referência: 0.4 - 4.0)
    *   T4 Livre: 1.2 ng/dL (referência: 0.8 - 1.8)
2.  **Hemograma Completo (01/12/2024):**
    *   Hemoglobina: 13.5 g/dL (normal)
    *   Leucócitos: 7.200/mm³ (normal)

---
**AVISO DE CONFIDENCIALIDADE:** Este resumo é uma demonstração. Em um cenário real, a manipulação de dados de prontuário exige o mais alto nível de segurança e conformidade com as regulamentações de privacidade de dados de saúde.

---

## 3. Resposta ao Prompt Estruturado (KERNEL) (Simulação GPT)

**Prompt:**
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

**Resultado Simulado GPT:**

**Nota:** O prontuário anonimizado não foi fornecido. Abaixo, um exemplo de como um modelo GPT estruturaria o resumo com base em dados fictícios, respeitando as restrições de privacidade.

### **Sumário Clínico do Paciente (Simulação)**

#### **1. Informações Demográficas**
*   **Identificador:** Paciente "R. Costa"
*   **Idade:** 42 anos
*   **Gênero:** Masculino

#### **2. Condições Crônicas**
*   Asma Brônquica (diagnóstico infantil, controlada)
*   Refluxo Gastroesofágico (RGE)

#### **3. Alergias**
*   Alergia a AINEs (Anti-inflamatórios Não Esteroides) - relata broncoespasmo.

#### **4. Histórico de Consultas Recentes (Últimas 3)**
*   **10/07/2025:** Queixa de pirose e regurgitação ácida. Prescrito Omeprazol 20mg/dia.
*   **05/04/2025:** Acompanhamento de rotina da asma. Sem exacerbações. Mantido Salbutamol SOS.
*   **20/11/2024:** Consulta para check-up geral. Solicitados exames de rotina.

#### **5. Exames Laboratoriais Relevantes (Últimos 2)**
*   **Endoscopia Digestiva Alta (01/07/2025):** Esofagite grau A, hérnia de hiato por deslizamento.
*   **Espirometria (01/04/2025):** Padrão ventilatório normal, sem obstrução.

---
**CONFIDENCIALIDADE GARANTIDA:** Este é um exemplo ilustrativo. Em um cenário real, a IA processaria os dados fornecidos com a máxima segurança e não reteria informações sensíveis.
---
