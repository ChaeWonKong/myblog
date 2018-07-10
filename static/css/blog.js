
const editor = {
	"text": document.getElementById('id_text'),
	"highlight": window.getSelection(),
	"path": ""
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
	}, 
	"insertImg": function() {
		if (this.path) {
			const cursorPos = this.text.selectionStart;
			const beforeStr = this.text.value.substring(0, cursorPos);
			const afterStr = this.text.value.substring(cursorPos, this.text.value.length);
			this.text.value = 
				beforeStr
				+ '<img src="http://leonkong.com/static'
				+ this.path
				+ '" style="max-width: 500px" />''
				+ afterStr;
		} else {
			alert('Oops! Upload First!');
		}
	}
};

const upload = {
	"getPath": function() {
		if (document.getElementById('img_src')){
			editor.path = document.getElementById('img_src');
		}
	},
	"openUpload": function() {
		window.open('http://www.leonkong.com/post/upload/', '_blank', 'width=550px, height=150px');
	},
	"closeUpload": function() {
		this.getPath();
		window.close();
	}
};

