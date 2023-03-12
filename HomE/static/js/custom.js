'use strict';

$(document).ready(function(){

    $(document).on("keypress", "#rent_filter_search", function() {
        var search_keyword = $(this).val();
        var rent_list;
        if (search_keyword.length > 3){

            $.ajax({
                url: "/search_rent_filter",
                dataType: 'json',
                data:{
                    "search_keyword": search_keyword
                },
                type:'GET',
                async: false,
                cache: false,
                timeout: 90000,
                success: function (data) {
                    rent_list = data.rent_list;
                },
                error: function(){
                    console.log("error");
                    }        
            });

            console.log("success");

            $('#tableWrapper').children('tbody').find('tr').remove();
            $('#tableWrapper').children('tbody').last().append(
                `<tr class="table-headder">
                <td>Rent ID</td>
                <td>Rent Month/Year</td>
                <td>Rent RecivedDate</td>
                <td>Rent Home</td>
                <td>Rent Tenent</td>
                <td>Rent Amount</td>
                </tr>`
            );
            for (var [key, value] of Object.entries(rent_list)) {
            
                    $('#tableWrapper')
                        .children('tbody')
                        .last().append(
                            `
                            <tr class="table-data">
                                <td><a href="rent_detail_modify/`+value[0]+`">`+value[0]+`</a></td>
                                <td>`+value[1]+`</td>
                                <td>`+value[2]+`</td>
                                <td>`+value[3]+`</td>
                                <td>`+value[4]+`</td>
                                <td>`+value[5]+`</td>
                            </tr>
                            `
                        );
              }
        
        }
    });

});
