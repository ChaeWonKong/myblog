
const editor = {
	"text": document.getElementById('id_text'),
	"codeBlock": function(lang) {
		this.text.value += '<br /><pre><code class="' + lang + '"></code></pre>';
	},
	"addBr": function() {
		this.text.value += "<br />";
	}
};