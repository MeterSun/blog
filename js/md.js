const LOG = !location.host.match('github.io');

// const postdir = LOG ? '.post':'https://github.com/MeterSun/myblog/raw/master/.post';
const postdir = 'post';

var mdToHTML = function(titlename, id) {
    // if(!titlename.match('.md$'))  titlename = titlename + '.md';
    
    $.get(postdir + '/' + titlename, function(markdown) {
        LOG && console.log(markdown);
        markdown = markdown.replace(/^---[\s\S]+?---/,"");
        LOG && console.log(markdown);
        editormd.markdownToHTML(id,{
            markdown: markdown, //+ "\r\n" + $("#append-test").text(),
            htmlDecode      : "link,style,script,iframe",  // you can filter tags decode
            // toc             : false,
            tocm: true, // Using [TOCM]
            // //tocContainer    : "#custom-toc-container", // 自定义 ToC 容器层
            // //gfm             : false,
            // //tocDropdown     : true,
            // // markdownSourceCode : true, // 是否保留 Markdown 源码，即是否删除保存源码的 Textarea 标签
            emoji: true,
            taskList: true,
            tex: true, // 默认不解析
            flowChart: true, // 默认不解析
            sequenceDiagram: true // 默认不解析
        });
        //console.log("返回一个 jQuery 实例 =>", testEditormdView);
        //console.log(testEditormdView.getMarkdown());      // 获取Markdown源码
    });
};

var getQueryString = function(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    return unescape(r[2]) || null;
}
