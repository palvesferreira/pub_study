<script>
  import { investments } from '$lib/parser';
</script>

<h1>Dashboard Financeiro</h1>

<table>
  <thead>
    <tr>
      <th>Usuário</th>
      <th>Instituição</th>
      <th>Título</th>
      <th>Valor Atual</th>
      <th>Valor Anterior</th>
      <th>Ganho (R$)</th>
      <th>%</th>
    </tr>
  </thead>
  <tbody>
    {#each investments as inv}
      <tr>
        <td>{inv.user}</td>
        <td>{inv.institution}</td>
        <td>{inv.name}</td>
        <td class="numeric">R$ {inv.value.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}</td>
        <td class="numeric">R$ {inv.previousValue.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}</td>
        <td class="numeric {inv.gain >= 0 ? 'positive' : 'negative'}">
          {inv.gain.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
        </td>
        <td class="numeric {inv.gainPercent >= 0 ? 'positive' : 'negative'}">
          {inv.gainPercent}%
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1em;
  }

  th, td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: right;
  }

  th {
    background-color: #f2f2f2;
    text-align: left;
  }

  .numeric {
    text-align: right;
  }

  .positive {
    color: green;
  }

  .negative {
    color: red;
  }
</style>