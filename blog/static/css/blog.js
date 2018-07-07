// Javascript for Blog
btn_js.addEventListener('click', function(){
	editor.codeBlock('javascript');
});

btn_py.addEventListener('click', function(){
	editor.codeBlock('python');
});

btn_br.addEventListener('click', function(){
	editor.addBr();
});


var editor = {
	"text": document.getElementById('id_text'),
	"codeBlock": function(lang) {
		this.text.value += '</br><pre><code class="' + lang + '"></code></pre>';
	},
	"addBr": function() {
		this.text.value += "<br />";
	}
};