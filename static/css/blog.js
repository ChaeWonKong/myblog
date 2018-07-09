
const editor = {
	"text": document.getElementById('id_text'),
	"highlight": window.getSelection(),
	"cursorPos": this.text.selectionStart,
	"beforeStr": this.text.value.substring(0, cursorPos),
	"afterStr": this.text.value.substring(cursorPos, text.value.length),
	"codeBlock": function(lang) {
		this.text.value = 
			this.beforeStr 
			+ '<br /><pre><code class="' 
			+ lang + '"></code></pre>' 
			+ this.afterStr;
	},
	"addBr": function() {
		this.text.value = 
			this.beforeStr
			+ "<br />"
			+ this.afterStr;
	},
	"makeBolder": function() {
		this.highlight = '<b>' + this.highlight + '</b>';
		this.text.value = this.text.value.replace(window.getSelection(), this.highlight);
	}
};