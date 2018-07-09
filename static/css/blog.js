
const editor = {
	"text": document.getElementById('id_text'),
	"highlight": window.getSelection(),
	"cursorPos": this.text.selectionStart,
	"beforeStr": this.text.value.substring(0, this.cursorPos),
	"afterStr": this.text.value.substring(this.cursorPos, this.text.value.length),
	"codeBlock": function(lang) {
		// const cursorPos = this.text.selectionStart;
		// const beforeStr = this.text.value.substring(0, cursorPos);
		// const afterStr = this.text.value.substring(cursorpos, this.text.value.length);
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