## Splink has three broad tasks

- Allow the user to tailor record comparisons to their data e.g. jaro_winker on names, date diff on date of birth
- Output corresponding SQL strings that represent the record linkage model
- Execute these SQL strings efficiently against the chosen backend

## Splink populates SQL-agnostic templates with dialect-specific SQL

Splink's core logic is specified in dialect agnostic SQL. These templates are then populated with:

Dialect-specific, user-customised SQL.

- Diealect-specific, because record linkage uses functions like `jaro_winkler` that are not common across SQL dialects
- User-customised because the user can choose e.g. their blocking rules and how different columns should be compared

For example, for blocking:

```sql
SELECT {cols to select}
FROM
input_table AS l
LEFT JOIN input_table AS r
ON {blocking rule}
```

Scoring:

```sql
SELECT
{CASE WHEN jaro_winkler(name_l, name_r) > 0.8
THEN 1
END
AS comparison_vector}
FROM
df_blocked
```

'Special cases':

- Seed
- How to take a random sample from a table

## Splink uses caching and materialisation to optimise the speed of execution

If Splink naitvely submitted all SQL generated to the chosen backend it would be slow because:

- Some SQL engines (e.g. Spark) optimise very long Common Table Expression (CTE) pipelines poorly (the long lineage problem)
- Some of Splink's algos are iterative and so can't be reasonably expressed as a single CTE pipeline
- Some expensive intermediate tables are needed many times, so need to be cached so they don't have to be repeated re-calculated

## Separeation of concerns:

- Writing settings dictionary
-

## Progress on Splink 4

```python
from splink.comparison_level_library import ExactMatchLevel
from splink.input_expression import InputExpression

ExactMatchLevel("first_name")

col = (
    InputExpression("first_name")
    .lower()
    .regex_extract("^[A-Z]{1,4}")
)

ExactMatchLevel(col)

ExactMatchLevel("lower(first_name)")
```

## Questions

- How does ibis handle a function like `jaro_winkler` (limited availablity and use)
- How does ibis handle UDFs (arbitrary fns registered against the backend)
-
