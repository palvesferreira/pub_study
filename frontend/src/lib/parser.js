import { rawData } from './data';

function parseData(raw) {
  const lines = raw.split('\n').filter(Boolean);
  const investments = [];

  let currentUser = null;
  let currentInstitution = null;

  for (let line of lines) {
    line = line.trim();
    if (!line) continue;

    // Linha com usuário/instituição
    const userMatch = line.match(/^(\w+)\s+(\w+)/);
    if (userMatch) {
      currentUser = userMatch[1];
      currentInstitution = userMatch[2];
      continue;
    }

    // Linha com dados do título/investimento
    const invMatch = line.match(/([\w\s\.]+)\s+(\d{1,3}(?:\.\d{3})*(?:\,\d{2})?)\s+(\d{1,3}(?:\.\d{3})*(?:\,\d{2})?)\s+([\-]?\d{1,3}(?:\.\d{3})*(?:\,\d{2})?)/);
    if (invMatch && currentUser && currentInstitution) {
      const name = invMatch[1].trim();
      const valueStr = invMatch[2].replace(/\./g, '').replace(',', '.');
      const prevValueStr = invMatch[3].replace(/\./g, '').replace(',', '.');
      const gainStr = invMatch[4].replace(/\./g, '').replace(',', '.');

      const value = parseFloat(valueStr) || 0;
      const previousValue = parseFloat(prevValueStr) || 0;
      const gain = parseFloat(gainStr) || 0;
      const gainPercent = ((gain / previousValue) * 100) || 0;

      investments.push({
        user: currentUser,
        institution: currentInstitution,
        name,
        value,
        previousValue,
        gain,
        gainPercent: gainPercent.toFixed(2)
      });
    }
  }

  return investments;
}

export const investments = parseData(rawData);