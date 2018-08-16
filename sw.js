self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('sync', (event) => {
  console.log('Sync event listener');
  if (event.tag === 'fetch_data') {
    console.log('Sync event listener - fetch_data');
    event.waitUntil(
      fetch('http://127.0.0.1:8002/')
        .then(response => response.json())
        .then(data => {console.log('data: ', data); return data;})
    );
  }
});