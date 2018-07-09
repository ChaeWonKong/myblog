
const editor = {
	"text": document.getElementById('id_text'),
	"highlight": window.getSelection(),
	"codeBlock": function(lang) {
		this.text.value += '<br /><pre><code class="' + lang + '"></code></pre>';
	},
	"addBr": function() {
		this.text.value += "<br />";
	},
	"makeBolder": function() {
		this.highlight = '<b>' + this.highlight + '</b>';
		this.text.value = this.text.value.replace(window.getSelection(), this.highlight);
	}
};