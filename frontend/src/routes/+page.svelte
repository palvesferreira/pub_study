<script>
  import { investments } from '$lib/parser';
  const total = investments.reduce((sum, i) => sum + i.value, 0);
</script>

<h1>Controle Financeiro Semanal</h1>
<p>Total atual: <strong>R$ {total.toFixed(2)}</strong></p>
<a href="/dashboard">Ver todos os investimentos</a>