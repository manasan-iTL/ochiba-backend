$(function(){
    let totalManagementElement = $('input#id_object_set-TOTAL_FORMS');
    let currentObjectCount = parseInt(totalManagementElement.val()); 
    const initialElement = $('input#id_object_set-INITIAL_FORMS');
    const initialValue = parseInt(initialElement.val());
    let invisibleCheckbox = [];
    let countDeletebutton = 0;
    const trash_icon ='<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/> <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/></svg>'

    /*デフォルトの削除のチェックボックスを非表示にし、削除ボタンを作成して追加している*/

    for (let i = 0; i < currentObjectCount; i++) {
        invisibleCheckbox.push('input#id_object_set-' + i + '-DELETE');
        console.log(invisibleCheckbox);
        $('input#id_object_set-' + i + '-DELETE').css({
            'display':'none',
        }); 
        let saveElement = 'id_object_set-' + i + '-DELETE';
        $("label[for='" + saveElement + "']").css({
            'display':'none',
        });

        let searchbuttonElement = $('input#id_object_set-' + i + '-DELETE').parent();
        let createdeletebutton = $('<button><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/> <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/></svg></button>').attr({
            "id":"remove" + i,
            "type":"button",
        });
        createdeletebutton.appendTo(searchbuttonElement);
        console.log(searchbuttonElement);
        // searchbuttonElement.attr('id','remove' + i);
        
    }
    
    /*オブジェクト追加ボタンを押したときの操作
    　主に必要な要素を作成してそれを追加しているだけ
    */
    $('button#add').on('click', function(){

        let formwrapper = $('<div></div>',{
            "class":"object-form form-mytop form-paddleft",
        });
        let discriptionLabel = $('<label>概要:</label>', {
           for:'id_object_set-' + currentObjectCount + '-discription',
        });

        let discriptionElement = $('<textarea>', {
            class:'form-item',
            placeholder:'ブックマークした記事の概要、メモを入力',
            name:'object_set-' + currentObjectCount + '-discription',
            id:'id_object_set-' + currentObjectCount + '-discription',
        });

        let titleLabel = $('<label>タイトル:</label>', {
           for: 'id_object_set-' + currentObjectCount + '-title',
        });

        let titleElement = $('<input>', {
            class:'form-item',
            type:'text',
            placeholder:'ブックマークした記事のタイトルを入力',
            maxlength:'100',
            name:'object_set-' + currentObjectCount + '-title',
            id:'id_object_set-' + currentObjectCount + '-title',
        });

        let urlLabel = $('<label>URL:</label>', {
           for: 'id_object_set-' + currentObjectCount + '-url',
        });

        let urlElement = $('<input>', {
            class:'form-item',
            type:'url',
            placeholder:'ブックマークした記事のURLを入力',
            maxlength:'200',
            name:'object_set-' + currentObjectCount + '-url',
            id:'id_object_set-' + currentObjectCount + '-url',
        });

        let deleteobjElement = $('<button>' + trash_icon + '</button>');
        $(deleteobjElement).attr({
            'class':'addremove',
            'type':'button',
        })
        let discriptionElementdiv = $('<div></div>', {"class":"object-field"}).append(discriptionLabel,discriptionElement);
        let titleElementdiv = $('<div></div>', {"class":"object-field"}).append(titleLabel,titleElement);
        let urlElementdiv = $('<div></div>', {"class":"object-field"}).append(urlLabel,urlElement);
        let deleteElementdiv = $('<div></div>', {"class":"object-field"}).append(deleteobjElement)
        
        let ele = $(formwrapper).append(urlElementdiv,titleElementdiv,discriptionElementdiv,deleteElementdiv);
        $('.edit-footer').before(ele);
        
        countDeletebutton += 1;
        currentObjectCount += 1;
        totalManagementElement.attr('value', currentObjectCount);
    });

    /*削除ボタン（DBに保存されていないObject）を押したときの操作*/
    $(document).on('click','.addremove', function(){
        console.log("click")
        $(this).parents('.object-form').remove();
    });
    
    

    /*削除ボタン（DBに保存されているObject）を押したときの操作*/
    for (let j = 0; j < currentObjectCount; j++){
        $('.object-form').on('click', '#remove'+ j, function(){
            let confirm = window.confirm('本当に削除しても良いですか？')
            if(confirm) {
                console.log('ok')
                $(invisibleCheckbox[j]).prop('checked', true);
                if ( $(invisibleCheckbox[j]).prop('checked') )
                    console.debug('チェックされていますよ (prop)');
                else
                console.debug('チェックされていませんよ (prop)');
                let tagetElement = $('#remove' + j).parents('.object-form');
                console.log(tagetElement);
                tagetElement.css('display', 'none'); 
            }
        });
    }
});