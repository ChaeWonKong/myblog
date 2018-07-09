
const editor = {
	"text": document.getElementById('id_text'),
	"highlight": window.getSelection(),
	"codeBlock": function(lang) {
		const cursorPos = this.text.selectionStart;
		const beforeStr = this.text.value.substring(0, cursorPos);
		const afterStr = this.text.value.substring(cursorPos, this.text.value.length);
		this.text.value = 
			beforeStr 
			+ '<br /><pre><code class="' 
			+ lang + '"></code></pre>' 
			+ afterStr;
	},
	"addBr": function() {
		const cursorPos = this.text.selectionStart;
		const beforeStr = this.text.value.substring(0, cursorPos);
		const afterStr = this.text.value.substring(cursorPos, this.text.value.length);
		this.text.value = 
			beforeStr
			+ "<br />"
			+ afterStr;
	},
	"makeBolder": function() {
		this.highlight = '<b>' + this.highlight + '</b>';
		this.text.value = this.text.value.replace(window.getSelection(), this.highlight);
	}, 
	"makeUnderLine": function() {
		this.highlight = '<u>' + this.highlight + '</u>';
		this.text.value = this.text.value.replace(window.getSelection(), this.highlight);
	}
};

function imgUpload() {
	window.open('http://www.leonkong.com/post/upload/', '_blank', 'width=550px, height=150px');
}