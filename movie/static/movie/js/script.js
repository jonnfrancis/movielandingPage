const showNavbar=(toggleId,navId,bodyId,headerId)=>{const toggle=document.getElementById(toggleId),nav=document.getElementById(navId),bodypd=document.getElementById(bodyId),headerpd=document.getElementById(headerId);if(toggle&&nav&&bodypd&&headerpd){toggle.addEventListener("click",()=>{nav.classList.toggle("show");toggle.classList.toggle("la-times");bodypd.classList.toggle("body-pd");headerpd.classList.toggle("body-pd")})}};showNavbar("header-toggle","nav-bar","body-pd","header");$(document).ready(function(){var path=window.location.pathname;if(path.includes("categories")){$("#tags-link").addClass("active")}else if(path.includes("actors")){$("#actors-link").addClass("active")}else if(path.includes("directors")){$("#directors-link").addClass("active")}else{$("#genres-link").addClass("active")}$(".nav__link").click(function(e){$(".nav__link").removeClass("active");$(this).addClass("active")})});$(document).ready(function(){$("#autoWidth,#autoWidth2").lightSlider({autoWidth:true,loop:true,controls:true,auto:true,pause:4e3,speed:1500,easing:"linear",onSliderLoad:function(){$("#autoWidth,#autoWidth2").removeClass("cS-hidden")}})});function toggle(){var trailer=document.querySelector(".trailer");var video=document.querySelector("iframe");trailer.classList.toggle("active");video.currentTime=0;video.pause()}$(".slider").slick({autoplay:false,speed:800,lazyload:"progressive",arrows:true,dots:false,prevArrow:'<div class="slick-nav prev-arrow"><i class="bx bx-chevron-r"></i></div>',nextArrow:'<div class="slick-nav next-arrow"><i class="bx bx-chevron-left"></i></div>',responsive:[{breakpoint:992,settings:{dots:true,arrows:false}}]}).slickAnimation();$(".slick-nav").on("click touch",{passive:true},function(e){e.preventDefault();var arrow=$(this);if(!arrow.hasClass("animate")){arrow.addClass("animate");setTimeout(()=>{arrow.removeClass("animate")},1600)}});$(document).ready(function(){function highlight(word,query){let check=new RegExp(query,"ig");return word.toString().replace(check,function(matchedText){return"<u style='background-color: #A5C9CA; text-decoration: none; padding: 3px; border-radius: 3px;'>"+matchedText+"</u>"})}$("#result-list").hide();$("#list").hide();$(".search-input").keyup(function(){let search=$(this).val();let results="";if(search==""){$("#result-list").hide();$(".search-input").removeClass("arrow").addClass("search")}else{$(".search-input").removeClass("search").addClass("arrow")}$.getJSON("https://www.omdbapi.com/?",{apikey:"365f49b1",s:search},function(data){if(data.Search!==undefined){$.each(data.Search,function(index,value){if(index<2){$.getJSON("https://www.omdbapi.com/?",{apikey:"365f49b1",i:value.imdbID},function(movieData){if(movieData){results+='<div class="result row p-1">';results+='<div class="col-sm-5 result-poster"><img src='+movieData.Poster+' " /></div>';results+='<div class="col-sm-7 text-left">';results+='<div class="movie-title">'+highlight(movieData.Title,$(".search-input").val())+" ("+movieData.Year+")</div>";results+='<div class="rating-div "><span class="badge h4 rating">'+movieData.imdbRating+"</span>/10</div>";results+='<div class="">';results+='<div class="rating-lang">Language: '+movieData.Language+"</div>";results+="</div>";results+='<div class="" style="padding-top: 5px;">';results+="<div>"+movieData.Plot.slice(0,50)+'... <a href="#">Details »</a></div>';results+="</div>";results+="</div>";results+="</div>";$("#results").html(results);if(/Mobi|Android/i.test(navigator.userAgent)){$("#results").children(".result").eq(1).hide()}else{$(".result").first().after("<hr>")}}})}});$("#result-list").show()}})});function handleSearch(e){e.preventDefault();var search=$(".search-input").val();let listResults="";$("#search").hide();$("#pass2").hide();$("#list").show();$("#search-term").html("Results for: "+search);$.getJSON("https://www.omdbapi.com/?",{apikey:"365f49b1",s:search},function(listData){if(/Mobi|Android/i.test(navigator.userAgent)){$("#list-count").html("("+listData.totalResults+")")}else{$("#list-count").html(listData.totalResults+" movie found")}if(listData.Search!==undefined){$.each(listData.Search,function(index,value){$.getJSON("https://www.omdbapi.com/?",{apikey:"365f49b1",i:value.imdbID},function(listMovieData){if(listMovieData){listResults+='<div class="list-result col-6 p-3">';listResults+='<div class="row" style="align-items: center;">';listResults+='<div class="col-md-6 movielink-poster" style=" display: flex; align-items: center; background: url('+listMovieData.Poster+');"><img src="'+listMovieData.Poster+'" style="width: 50%; border-radius: 3px; position: relative; z-index: 1; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);" class="poster-img " /></div>';listResults+='<div class="col-md-6 my-3 text-left">';listResults+='<div class="movie-title" style="color: white;">'+highlight(listMovieData.Title,$(".search-input").val())+" ("+listMovieData.Year+")</div>";listResults+='<div class="rating-div" style="color: white; padding-top: 5px;"><i class="bx bxs-star" style="color: #2C74B3; font-size: 24px; margin-right: 3px;"></i><span class="h4 rating" style="color: #A5C9CA; font-weight: 700; ">'+listMovieData.imdbRating+"</span>/10</div>";listResults+='<div class="my-3" style="background: rgba(26, 55, 77, 0.5); border-radius: 7px; padding-block: 7px; padding-inline: 10px;">';listResults+='<div style="color: white;"><strong>Language:</strong> '+listMovieData.Language+"</div>";listResults+='<div style="color: white;"><strong>Stars:</strong> '+listMovieData.Actors.split(",").slice(0,3)+"</div>";listResults+='<div style="color: white;"><strong>Genre:</strong> '+listMovieData.Genre.split(",").slice(0,3)+"</div>";listResults+="</div>";listResults+='<div class="my-3">';listResults+='<div style="color: rgb(231, 246, 242); display: -webkit-box; -webkit-line-clamp: 6; overflow: hidden; text-overflow: ellipsis;">'+listMovieData.Plot+"</div>";listResults+="</div>";listResults+="</div>";listResults+="</div>";listResults+="</div>";$("#list-results").html(listResults);$(".list-result:odd:not(:last-child)").after("<div class='col-12'><hr></div>")}})})}})}$("#show-more").click(function(e){handleSearch(e)});$(".search-input").keydown(function(e){if(e.key==="Enter"){handleSearch(e)}});$("#searchAgain").click(function(){$("#search").show();$("#list").hide();$("#result-list").hide();$(".search-input").val("");$("#pass2").show()})});$(function(){$(".search-input").popover({title:"WAIT!!!",content:"You can't do that. Go search from home😅"}).blur(function(){$(this).popover("hide")})});document.addEventListener("DOMContentLoaded",function(){const loadMoreBtn=document.getElementById("load-more-actors");let displayedActors=14;loadMoreBtn.addEventListener("click",function(e){e.preventDefault();const hiddenMovies=document.querySelectorAll("#tagsh .category-list .actors-box.hidden");for(let i=0;i<12&&i<hiddenMovies.length;i++){hiddenMovies[i].classList.remove("hidden")}displayedActors+=6;if(hiddenMovies.length<=6){loadMoreBtn.style.display="none"}})});