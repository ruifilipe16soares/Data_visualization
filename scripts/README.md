# Data Transformation Scripts

With the database schema now replicated as indices in **Elasticsearch**, and with real-time events being properly mirrored,  
we could already build some basic visualizations to expose our data.  
However, this replication process introduces a few important challenges:

---

## Replication Challenges

- **Elasticsearch does not support relationships between indices**, unlike MySQL which allows table relationships through `JOIN`s.
- Without this capability, it becomes significantly harder to analyze and correlate information coming from the database.

For example:  
Imagine a schema containing two tables — **motorista** (driver) and **veiculo** (vehicle).

---

### Example Tables

#### motoristas
![Motoristas Table](/mnt/data/ab7f4762-c4ed-4370-91c5-b489507f50d5.png)

#### veiculos
![Veiculos Table](/mnt/data/23e5b501-80b4-4469-9fa0-3b869276cb8c.png)


#### motoristas

| id | nome           | email                 | telefone       | cnh       | veiculo_id | disponivel | avaliacao_media | criado_em           |
|----|----------------|----------------------|----------------|-----------|-------------|-------------|------------------|---------------------|
| 1  | João Silva     | joao.silva@email.com | (11) 99999-1111 | CNH123456 | 1           | 1           | 4.80             | 2025-11-15 22:47:21 |
| 2  | Maria Santos   | maria.santos@email.com | (11) 99999-2222 | CNH654321 | 2           | 1           | 4.90             | 2025-11-15 22:47:21 |
| 3  | Pedro Oliveira | pedro.oliveira@email.com | (11) 99999-3333 | CNH987654 | 3           | 0           | 4.70             | 2025-11-15 22:47:21 |

#### veiculos

| id | marca   | modelo  | ano  | placa   | cor    | capacidade_passageiros |
|----|---------|----------|------|---------|--------|-------------------------|
| 1  | Toyota  | Corolla  | 2022 | ABC1D23 | Prata  | 4                       |
| 2  | Honda   | Civic    | 2021 | XYZ4E56 | Preto  | 4                       |
| 3  | Hyundai | HB20     | 2023 | DEF7G89 | Branco | 4                       |

---

The **motorista** table has a column `veiculo_id` that references the **veiculo** table.  
If we wanted, for example, to create a chart showing the **top 5 most common car brands among drivers**,  
we would need to combine information from both tables.

In SQL, we could easily achieve this with a `JOIN`:

```sql
SELECT 
    m.nome AS motorista,
    v.marca AS marca_veiculo,
    v.modelo AS modelo_veiculo
FROM motoristas m
INNER JOIN veiculos v ON m.veiculo_id = v.id;
```
---

## Limitation in Elasticsearch

Elasticsearch does not support joins between indices, so this kind of relational query is **not possible directly**.

---

## Why We Need Data Transformation Scripts

To overcome this limitation — and also to address other issues such as:

- Date and timezone formatting  
- Adding computed or derived fields  
- Enriching indices with related information  

—we created **Python transformation scripts** to process and combine data after ingestion.

These scripts make building dashboards much easier and provide cleaner, more meaningful datasets for visualization.

---

### Example

The file **`combine_index.py`** demonstrates a simple example of how this data merging and enrichment can be performed.

