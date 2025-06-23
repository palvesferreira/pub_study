<script>
  import { token } from '../stores/authStore';
  import { API_BASE_URL } from '$lib/api';
  /**
   * @typedef {{ title: { code: string }, value: number }} Quote
   */

  /** @type {Quote[]} */
  let quotes = [];

  async function fetchQuotes() {
    const res = await fetch(`${API_BASE_URL}quotes`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    /** @type {Quote[]} */
    quotes = await res.json();
  }

  fetchQuotes();
</script>

<h2>Dashboard</h2>
<ul>
  {#each quotes as quote}
    <li>{quote.title.code} - R$ {quote.value.toFixed(2)}</li>
  {/each}
</ul>