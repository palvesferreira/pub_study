<script>
  let title = {
    code: '',
    description: '',
    type_title: '',
    institution_id: ''
  };

  async function saveTitle() {
    const res = await fetch('http://localhost:8000/titles/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(title)
    });
    if (res.ok) alert('Título salvo!');
  }
</script>

<form on:submit|preventDefault={saveTitle}>
  <input bind:value={title.code} placeholder="Código" />
  <input bind:value={title.description} placeholder="Descrição" />
  <input bind:value={title.type_title} placeholder="Tipo" />
  <input type="number" bind:value={title.institution_id} placeholder="ID Instituição" />
  <button type="submit">Salvar</button>
</form>