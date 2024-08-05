document.getElementById('summarize-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(this);
  fetch('https://summarzy.vercel.app/summarize', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    document.getElementById('summary').innerText = data.summary;
  })
  .catch(error => {
    console.error('Error:', error);
    document.getElementById('summary').innerText = `Error summarizing text: ${error.message}`;
  });
});
