// Javascript for Blog
const js_code = document.getElementById('js_code');
const py_code = document.getElementById('py_code');

js_code.addEventListener('click', code.codeBlock('javascript'));
py_code.addEventListener('click', code.codeBlock('python'));

let code = {
	"text": document.getElementById('id_text'),
	"codeBlock": function(lang) {
		this.text.value += '</br><pre><code class="' + lang + '"></code></pre>';
	}
}