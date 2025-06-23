<script>
  import { token, setToken } from '../stores/authStore';
  let username = '';
  let password = '';
  let error = '';

  async function login() {
    const res = await fetch('http://localhost:8000/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    if (!res.ok) return error = data.detail;
    setToken(data.access_token);
    window.location.href = '/dashboard';
  }
</script>

<h2>Login</h2>
<input bind:value={username} placeholder="Usuário" />
<input type="password" bind:value={password} placeholder="Senha" />
<button on:click={login}>Entrar</button>
{#if error}<p style="color:red">{error}</p>{/if}