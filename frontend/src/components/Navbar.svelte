<script>
  import { token, clearAuth } from '../stores/authStore';
</script>

<nav>
  <a href="/">Home</a>
  {#if $token}
    <a href="/dashboard">Dashboard</a>
    <button on:click={() => clearAuth()}>Sair</button>
  {:else}
    <a href="/login">Login</a>
    <a href="/register">Registrar</a>
  {/if}
</nav>