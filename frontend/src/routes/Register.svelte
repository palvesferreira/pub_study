<script>
  let username = '';
  let password = '';
  let error = '';

  async function register() {
    const res = await fetch('http://localhost:8000/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    if (!res.ok) {
      const data = await res.json();
      error = data.detail;
      return;
    }
    alert('Cadastro realizado!');
    window.location.href = '/login';
  }
</script>

<h2>Cadastrar</h2>
<input bind:value={username} placeholder="Usuário" />
<input type="password" bind:value={password} placeholder="Senha" />
<button on:click={register}>Cadastrar</button>
{#if error}<p style="color:red">{error}</p>{/if}