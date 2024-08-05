document.getElementById('summarize-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('http://127.0.0.1:5000/summarize', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('summary').innerText = data.summary;
    })
    .catch(error => {
      console.error('Error:', error);
      document.getElementById('summary').innerText = 'Error summarizing text.';
    });
  });
