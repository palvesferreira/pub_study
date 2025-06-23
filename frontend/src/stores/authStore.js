import { writable } from 'svelte/store';

export const user = writable(null);
export const token = writable(localStorage.getItem('token') || null);

export const setToken = (newToken) => {
  localStorage.setItem('token', newToken);
  token.set(newToken);
};

export const clearAuth = () => {
  localStorage.removeItem('token');
  token.set(null);
  user.set(null);
};