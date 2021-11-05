/*** show navbar ***/
const showNavbar = (toggleId, navId, bodyId, headerId) => {
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)


    // validate the variables //
    if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
            //show navbar
            nav.classList.toggle('show')
            //change icon
            toggle.classList.toggle('la-times')
            //add pading to body
            bodypd.classList.toggle('body-pd')
            //add padding to header
            headerpd.classList.toggle('body-pd')
        })
    }
}

showNavbar('header-toggle', 'nav-bar', 'body-pd', 'header')

/*** link active ***/
const linkColor = document.querySelectorAll('.nav__link')

function colorLink(){
    if (linkColor){
        linkColor.forEach(l => l.classList.remove('active'))
        this.classList.add('active')
    }
}

linkColor.forEach(l => l.addEventListener('click', colorLink))


$(document).ready(function() {
    $('#autoWidth,#autoWidth2').lightSlider({
        autoWidth:true,
        loop:true,
        onSliderLoad: function() {
            $('#autoWidth,#autoWidth2').removeClass('cS-hidden');
        } 
    });  
});

function toggle(){
    var trailer = document.querySelector('.trailer');
    var video = document.querySelector('iframe');
    trailer.classList.toggle('active')
    video.currentTime = 0;
    video.pause()
}

$('.slider').slick({
    autoplay : false,
    speed : 800,
    lazyload : 'progressive',
    arrows : true,
    dots : false,
    prevArrow : '<div class="slick-nav prev-arrow"><i class="bx bx-chevron-r"></i></div>',
    nextArrow : '<div class="slick-nav next-arrow"><i class="bx bx-chevron-left"></i></div>',
    responsive : [
        {
            breakpoint : 992,
            settings : {
                dots : true,
                arrows : false,
            }
        }
    ]
}).slickAnimation();
$(".slick-nav").on("click touch",{passive: true}, function (e){
    e.preventDefault();

    var arrow = $(this);

    if(!arrow.hasClass('animate')){
        arrow.addClass('animate');
        setTimeout(() => {
            arrow.removeClass('animate');
        }, 1600);
    }
});
/*
var data;
function getanswer(q){
$.get("https://www.omdbapi.com/?s="+q+"&apikey=365f49b1", function(rawdata){
var rawstring =JSON.stringify(rawdata);
console.log(rawstring);
data =JSON.parse(rawstring);
var title = data.Search[0].Title;
var year = data.Search[0].Year; 
var imdburl="https://www.imdb.com/title/"+data.Search[0].imdbID+"/";

var posterurl =data.Search[0].Poster;
var rating = data.Search[0].Rated;
document.getElementById('pass').innerHTML="<h1>"+title+"</h1><br> <img src= '"+posterurl+"'><br><p> Year Released:"+year+"</p> <br> <p> Rating: "+rating+"</p> <br> <p> IMDB page: <a href='"+imdburl+"'target='_blank'>"+imdburl+"</a></p>"; }); }
*/

/*
$(document).ready(function() {

    var apikey = "365f49b1"
    $("#movieForm").submit(function(event) {
        event.preventDefault() 

        var movie = $("#movie").val()
        var result = ""
        var url = "http://www.omdbapi.com/?apikey="+apikey

        $.ajax({
            method: 'GET',
            url:url+"&s="+movie,
            success: function(data) {
                for (const movie in data){
                   console.log(movie) 
            }
                
                $("#pass").html(result);
            }
        })

        
    })
})
*/
$(document).ready(function() {

    function highlight(word, query) {
        let check = new RegExp(query, "ig")
        return word.toString().replace(check, function(matchedText) {
            return "<u style='background-color: yellow'>" + matchedText + "</u>"
        })
    }

    $("#result-list").hide()
    $("#list").hide()

    $(".search-input").keyup(function() {
        let search = $(this).val()
        let results = ""
        if (search == "") {
            $("#result-list").hide()
            $(".search-input").removeClass("arrow").addClass("search")
        } else {
            $(".search-input").removeClass("search").addClass("arrow")
        }

        $.getJSON("https://www.omdbapi.com/?", { apikey: "365f49b1", s: search }, function(data) {
            if (data.Search !== undefined) {
                $.each(data.Search, function(index, value) {
                    if (index < 2) {
                        $.getJSON("https://www.omdbapi.com/?", { apikey: "365f49b1", i: value.imdbID }, function(movieData) {
                            if (movieData) {
                                results += '<div class="result row p-1">'
                                results += '<div class="col-sm-5"><img src=' + movieData.Poster + ' style="width: 170px; height: 250px;" /></div>'
                                results += '<div class="col-sm-7 text-left">'
                                results += '<div class="movie-title">'+ highlight(movieData.Title, $(".search-input").val()) +' ('+ movieData.Year +')</div>'
                                results += '<div class="rating-div"><span class="h4 rating">'+ movieData.imdbRating +'</span>/10</div>'
                                results += '<div class="my-3">'
                                results += '<div>Language: '+ movieData.Language + '</div>'
                                results += '<div>Stars: '+ movieData.Actors.split(",").slice(0, 3) + ' | <a href="#">Show All »</a></div>'
                                results += '</div>'
                                results += '<div class="my-3">'
                                results += '<div>'+ movieData.Plot.slice(0, 100) + '... <a href="#">Details »</a></div>'
                                results += '</div>'
                                results += '</div>'
                                results += "</div>"
                                $("#results").html(results)
                                
                                if (/Mobi|Android/i.test(navigator.userAgent)) {
                                    $("#results").children(".result").eq(1).hide();
                                } else {
                                    $(".result").first().after("<hr>")
                                }
                            }
                        })
                    }
                });
                $("#result-list").show()
            }
        });
    });
    
    $("#show-more").click(function(e) {
        e.preventDefault()
        var search = $(".search-input").val()
        let listResults = ""
        $("#search").hide()
        $("#pass2").hide()
        $("#list").show()
        $("#search-term").html("Results for: " + search)
        $.getJSON("https://www.omdbapi.com/?", { apikey: "365f49b1", s: search }, function(listData) {
            if (/Mobi|Android/i.test(navigator.userAgent)) {
                $("#list-count").html("(" + listData.totalResults + ")")
            } else {
                $("#list-count").html(listData.totalResults + " movie found")
            }
            if (listData.Search !== undefined) {
                $.each(listData.Search, function(index, value) {
                    $.getJSON("https://www.omdbapi.com/?", { apikey: "365f49b1", i: value.imdbID }, function(listMovieData) {
                        if (listMovieData) {
                            listResults += '<div class="list-result col-6 p-3">'
                            listResults += '<div class="row">'
                            listResults += '<div class="col-md-6 movielink"><img src="' + listMovieData.Poster + '" style="width: 100%;" /></div>'
                            listResults += '<div class="col-md-6 text-left">'
                            listResults += '<div class="movie-title">'+ highlight(listMovieData.Title, $(".search-input").val()) +' ('+ listMovieData.Year +')</div>'
                            listResults += '<div class="rating-div"><span class="h4 rating">'+ listMovieData.imdbRating +'</span>/10</div>'
                            listResults += '<div class="my-3">'
                            listResults += '<div>Language: '+ listMovieData.Language + '</div>'
                            listResults += '<div>Stars: '+ listMovieData.Actors.split(",").slice(0, 3) + ' | <a href="#">Show All »</a></div>'
                            listResults += '</div>'
                            listResults += '<div class="my-3">'
                            listResults += '<div>'+ listMovieData.Plot.slice(0, 100) + '... <a href="#">Details »</a></div>'
                            listResults += '</div>'
                            listResults += '</div>' // col-6 end
                            listResults += "</div>" // row end
                            listResults += "</div>" // list-result col-6 end
                            $("#list-results").html(listResults)
                            $(".list-result:odd:not(:last-child)").after("<div class='col-12'><hr></div>")
                        }
                    })
                });
            }
        });
    });

    $("#searchAgain").click(function() {
        $("#search").show()
        $("#list").hide()
        $("#result-list").hide()
        $(".search-input").val("")
        $("#pass2").val("")
    });
});

$(function () {
    $(".search-input")
        .popover({ title: 'WAIT!!!', content: "You can't do that. Go search from the homepage ;)" })
        .blur(function () {
            $(this).popover('hide');
        });
});

