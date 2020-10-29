from django.http import HttpResponse
import os
def index(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <title>SELLTON</title>
    </head>
    <body>
    <header class="text-gray-700 body-font">
      <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-teal-500 rounded-full" viewBox="0 0 24 24">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
          </svg>
          <a href ="http://127.0.0.1:8000/" class="ml-3 text-xl">SELLTON</a>
        </a>
        <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
          <a  href ="http://127.0.0.1:8000/" class="mr-5 hover:text-gray-900">HOME</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features" class="mr-5 hover:text-gray-900">FEATURES</a>
          <a  href ="http://127.0.0.1:8000/gallery" class="mr-5 hover:text-gray-900">GALERY</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us" class="mr-5 hover:text-gray-900">ABOUT US</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact" class="mr-5 hover:text-gray-900">CONTACT US</a>
        </nav>
       <div class="topnav">
        <input type="text" placeholder=" Search " >
      </div>
        <button class="inline-flex items-center bg-gray-200 border-0 py-1 px-3 focus:outline-none hover:bg-gray-300 rounded text-base mt-4 md:mt-0" type="submit" value="Search" onclick="window.location.href='gallery/about_us/contact/Features/Maintenance'">Search
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>
    </header>
    <hr>
        <section class="text-gray-700 body-font">
            <div class="container px-5 py-24 mx-auto">
              <div class="flex flex-wrap -m-4">
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1549298916-b41d501d3772?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=260&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=420">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">SHOES</h2>
                    <p class="mt-1">$16.00</p>
                  </div>
                </div>
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1444881421460-d838c3b98f95?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=261&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=421">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">WATCH</h2>
                    <p class="mt-1">$21.15</p>
                  </div>
                </div>
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1545776771-0a6367761ff3?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=262&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=422">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">BAG</h2>
                    <p class="mt-1">$12.00</p>
                  </div>
                </div>
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1553704571-c32d20e6c74f?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=263&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=423">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">BELT</h2>
                    <p class="mt-1">$18.40</p>
                  </div>
                </div>
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1545596281-a183a368b1d0?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=264&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=424">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">SHIRT</h2>
                    <p class="mt-1">$16.00</p>
                  </div>
                </div>
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1454720503269-3a35c21bebc6?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=265&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=425">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">TROUSER</h2>
                    <p class="mt-1">$21.15</p>
                  </div>
                </div>
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1561814648-28c884af83c0?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=266&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=426">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">Hat</h2>
                    <p class="mt-1">$12.00</p>
                  </div>
                </div>
                <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                  <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance" class="block relative h-48 rounded overflow-hidden">
                    <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://images.unsplash.com/photo-1541108564883-bec8126021f5?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=267&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=427">
                  </a>
                  <div class="mt-4">
                    <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                    <h2 class="text-gray-900 title-font text-lg font-medium">PERFUME</h2>
                    <p class="mt-1">$18.40</p>
                  </div>
                </div>
              </div>
            </div>
          </section>

    </body>
    </html>
    ''')



#html response  for about_us page 
def about_us(request):
    # path=os.path.dirname(__file__)
    # f=open(f"{path}\one.txt","r")
    # return HttpResponse(f.read())
    return HttpResponse('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <title>ABOUT US</title>
    </head>
    <body>
          <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-teal-500 rounded-full" viewBox="0 0 24 24">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
          </svg>
          <a href ="http://127.0.0.1:8000/" class="ml-3 text-xl">SELLTON</a>
        </a>
        <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
          <a  href ="http://127.0.0.1:8000/" class="mr-5 hover:text-gray-900">HOME</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features" class="mr-5 hover:text-gray-900">FEATURES</a>
          <a  href ="http://127.0.0.1:8000/gallery" class="mr-5 hover:text-gray-900">GALERY</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us" class="mr-5 hover:text-gray-900">ABOUT US</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact" class="mr-5 hover:text-gray-900">CONTACT US</a>
        </nav>
       <div class="topnav">
       <hr>
      <section class="text-gray-700 body-font">
        <div class="container px-5 py-24 mx-auto flex flex-wrap">
          <div class="flex flex-wrap -mx-4 mt-auto mb-auto lg:w-1/2 sm:w-2/3 content-start sm:pr-10">
            <div class="w-full sm:p-4 px-4 mb-6">
              <h1 class="title-font font-medium text-xl mb-2 text-gray-900">Moon hashtag pop-up try-hard offal truffaut</h1>
              <div class="leading-relaxed">Pour-over craft beer pug drinking vinegar live-edge gastropub, keytar neutra sustainable fingerstache kickstarter.</div>
            </div>
            <div class="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
              <h2 class="title-font font-medium text-3xl text-gray-900">2.7K</h2>
              <p class="leading-relaxed">Users</p>
            </div>
            <div class="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
              <h2 class="title-font font-medium text-3xl text-gray-900">1.8K</h2>
              <p class="leading-relaxed">Subscribes</p>
            </div>
            <div class="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
              <h2 class="title-font font-medium text-3xl text-gray-900">35</h2>
              <p class="leading-relaxed">Downloads</p>
            </div>
            <div class="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
              <h2 class="title-font font-medium text-3xl text-gray-900">4</h2>
              <p class="leading-relaxed">Products</p>
            </div>
          </div>
          <div class="lg:w-1/2 sm:w-1/3 w-full rounded-lg overflow-hidden mt-6 sm:mt-0">
            <img class="object-cover object-center w-full h-full" src="https://dummyimage.com/600x300" alt="stats">
          </div>
        </div>

      </section>

                <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
          <a class="text-gray-500"><svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z">

            </path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <rect width="20" height="20" x="2" y="2" rx="5" ry="5">

            </rect>
            <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37zm1.5-4.87h.01">

            </path>
            /svg>
          </a>
          <a class="ml-3 text-gray-500">
            <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" class="w-5 h-5" viewBox="0 0 24 24">
              <path stroke="none" d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z">

              </path>
              <circle cx="4" cy="4" r="2" stroke="none">

              </circle>
            </svg>
          </a>
        </span>
    </body>
    </html>
    
    ''')




#html response for the gallery page
def gallery(request):
    return HttpResponse('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <title>GALLERY</title>
    </head>
    <body>
              <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-teal-500 rounded-full" viewBox="0 0 24 24">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
          </svg>
          <a href ="http://127.0.0.1:8000/" class="ml-3 text-xl">SELLTON</a>
        </a>
        <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
          <a  href ="http://127.0.0.1:8000/" class="mr-5 hover:text-gray-900">HOME</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features" class="mr-5 hover:text-gray-900">FEATURES</a>
          <a  href ="http://127.0.0.1:8000/gallery" class="mr-5 hover:text-gray-900">GALERY</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us" class="mr-5 hover:text-gray-900">ABOUT US</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact" class="mr-5 hover:text-gray-900">CONTACT US</a>
        </nav>
       <div class="topnav">
       <hr>
      <section class="text-gray-700 body-font">
        <div class="container px-5 py-24 mx-auto flex flex-wrap">
          <div class="flex w-full mb-20 flex-wrap">
            <h1 class="sm:text-3xl text-2xl font-medium title-font text-gray-900 lg:w-1/3 lg:mb-0 mb-4">Master Cleanse Reliac Heirloom</h1>
            <p class="lg:pl-6 lg:w-2/3 mx-auto leading-relaxed text-base">Whatever cardigan tote bag tumblr hexagon brooklyn asymmetrical gentrify, subway tile poke farm-to-table. Franzen you probably haven't heard of them man bun deep jianbing selfies heirloom.</p>
          </div>
          <div class="flex flex-wrap md:-m-2 -m-1">
            <div class="flex flex-wrap w-1/2">
              <div class="md:p-2 p-1 w-1/2">
                <img alt="gallery" class="w-full object-cover h-full object-center block" src="https://images.unsplash.com/photo-1449247666642-264389f5f5b1?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=300&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=500">
              </div>
              <div class="md:p-2 p-1 w-1/2">
                <img alt="gallery" class="w-full object-cover h-full object-center block" src="https://images.unsplash.com/photo-1558401549-29b4893f4d9a?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=301&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=501">
              </div>
              <div class="md:p-2 p-1 w-full">
                <img alt="gallery" class="w-full h-full object-cover object-center block" src="https://dummyimage.com/600x360">
              </div>
            </div>
            <div class="flex flex-wrap w-1/2">
              <div class="md:p-2 p-1 w-full">
                <img alt="gallery" class="w-full h-full object-cover object-center block" src="https://dummyimage.com/601x361">
              </div>
              <div class="md:p-2 p-1 w-1/2">
                <img alt="gallery" class="w-full object-cover h-full object-center block" src="https://dummyimage.com/502x302">
              </div>
              <div class="md:p-2 p-1 w-1/2">
                <img alt="gallery" class="w-full object-cover h-full object-center block" src="https://dummyimage.com/503x303">
              </div>
            </div>
          </div>
        </div>

      </section>


                <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
          <a class="text-gray-500"><svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z">

            </path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <rect width="20" height="20" x="2" y="2" rx="5" ry="5">

            </rect>
            <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37zm1.5-4.87h.01">

            </path>
            /svg>
          </a>
          <a class="ml-3 text-gray-500">
            <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" class="w-5 h-5" viewBox="0 0 24 24">
              <path stroke="none" d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z">

              </path>
              <circle cx="4" cy="4" r="2" stroke="none">

              </circle>
            </svg>
          </a>
        </span>
    </body>
    </html>''')




#html response for the contact page
def contact(request):
    return HttpResponse('''
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
          <title>CONTACT US</title>
      </head>
      <body>
                <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-teal-500 rounded-full" viewBox="0 0 24 24">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
          </svg>
          <a href ="http://127.0.0.1:8000/" class="ml-3 text-xl">SELLTON</a>
        </a>
        <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
          <a  href ="http://127.0.0.1:8000/" class="mr-5 hover:text-gray-900">HOME</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features" class="mr-5 hover:text-gray-900">FEATURES</a>
          <a  href ="http://127.0.0.1:8000/gallery" class="mr-5 hover:text-gray-900">GALERY</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us" class="mr-5 hover:text-gray-900">ABOUT US</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact" class="mr-5 hover:text-gray-900">CONTACT US</a>
        </nav>
       <div class="topnav">
       <hr>
        <section class="text-gray-700 body-font relative">
          <div class="container px-5 py-24 mx-auto flex sm:flex-no-wrap flex-wrap">
            <div class="lg:w-2/3 md:w-1/2 bg-gray-300 rounded-lg overflow-hidden sm:mr-10 p-10 flex items-end justify-start relative">
              <iframe width="100%" height="100%" class="absolute inset-0" frameborder="0" title="map" marginheight="0" marginwidth="0" scrolling="no" src="https://maps.google.com/maps?width=100%&height=600&hl=en&q=%C4%B0zmir+(My%20Business%20Name)&ie=UTF8&t=&z=14&iwloc=B&output=embed" style="filter: grayscale(1) contrast(1.2) opacity(0.4);"></iframe>
              <div class="bg-white relative flex flex-wrap py-6">
                <div class="lg:w-1/2 px-6">
                  <h2 class="title-font font-medium text-gray-900 tracking-widest text-sm">ADDRESS</h2>
                  <p class="leading-relaxed">Photo booth tattooed prism, portland taiyaki hoodie neutra typewriter</p>
                </div>
                <div class="lg:w-1/2 px-6 mt-4 lg:mt-0">
                  <h2 class="title-font font-medium text-gray-900 tracking-widest text-sm">EMAIL</h2>
                  <a class="text-indigo-500 leading-relaxed">Sellton_India@gmail.com</a>
                  <h2 class="title-font font-medium text-gray-900 tracking-widest text-sm mt-4">PHONE</h2>
                  <p class="leading-relaxed">123-456-7890</p>
                </div>
              </div>
            </div>
            <div class="lg:w-1/3 md:w-1/2 bg-white flex flex-col md:ml-auto w-full md:py-8 mt-8 md:mt-0">
              <h2 class="text-gray-900 text-lg mb-1 font-medium title-font">Feedback</h2>
              <p class="leading-relaxed mb-5 text-gray-600">Post-ironic portland shabby chic echo park, banjo fashion axe</p>
              <input class="bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4" placeholder="Name" type="text">
              <input class="bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4" placeholder="Email" type="email">
              <textarea class="bg-white rounded border border-gray-400 focus:outline-none h-32 focus:border-indigo-500 text-base px-4 py-2 mb-4 resize-none" placeholder="Message"></textarea>
              <button class="text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg" onclick="window.location.href='http://127.0.0.1:8000/gallery/about_us/contact/Features/Maintenance'">Submit</button>
              <p class="text-xs text-gray-500 mt-3">Chicharrones blog helvetica normcore iceland tousled brook viral artisan.</p>
            </div>
          </div>

        </section>

        <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
          <a class="text-gray-500"><svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z">

            </path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <rect width="20" height="20" x="2" y="2" rx="5" ry="5">

            </rect>
            <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37zm1.5-4.87h.01">

            </path>
            /svg>
          </a>
          <a class="ml-3 text-gray-500">
            <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" class="w-5 h-5" viewBox="0 0 24 24">
              <path stroke="none" d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z">

              </path>
              <circle cx="4" cy="4" r="2" stroke="none">

              </circle>
            </svg>
          </a>
        </span>

    </body>
    </html>
    ''')

def Features(request):
    return HttpResponse('''
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
          <title>FEATURES</title>
      </head>
      <body>
                <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-teal-500 rounded-full" viewBox="0 0 24 24">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
          </svg>
          <a href ="http://127.0.0.1:8000/" class="ml-3 text-xl">SELLTON</a>
        </a>
        <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
          <a  href ="http://127.0.0.1:8000/" class="mr-5 hover:text-gray-900">HOME</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features" class="mr-5 hover:text-gray-900">FEATURES</a>
          <a  href ="http://127.0.0.1:8000/gallery" class="mr-5 hover:text-gray-900">GALERY</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us" class="mr-5 hover:text-gray-900">ABOUT US</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact" class="mr-5 hover:text-gray-900">CONTACT US</a>
        </nav>
       <div class="topnav">
       <hr>
        <section class="text-gray-700 body-font">
          <div class="container px-5 py-24 mx-auto">
            <div class="flex flex-col text-center w-full mb-20">
              <h2 class="text-xs text-indigo-500 tracking-widest font-medium title-font mb-1">ROOF PARTY POLAROID</h2>
              <h1 class="sm:text-3xl text-2xl font-medium title-font text-gray-900">Master Cleanse Reliac Heirloom</h1>
            </div>
            <div class="flex flex-wrap -m-4">
              <div class="p-4 md:w-1/3">
                <div class="flex rounded-lg h-full bg-gray-100 p-8 flex-col">
                  <div class="flex items-center mb-3">
                    <div class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full bg-indigo-500 text-white flex-shrink-0">
                      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                        <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                      </svg>
                    </div>
                    <h2 class="text-gray-900 text-lg title-font font-medium">Shooting Stars</h2>
                  </div>
                  <div class="flex-grow">
                    <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.</p>
                    <a class="mt-3 text-indigo-500 inline-flex items-center">Learn More
                      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                        <path d="M5 12h14M12 5l7 7-7 7"></path>
                      </svg>
                    </a>
                  </div>
                </div>
              </div>
              <div class="p-4 md:w-1/3">
                <div class="flex rounded-lg h-full bg-gray-100 p-8 flex-col">
                  <div class="flex items-center mb-3">
                    <div class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full bg-indigo-500 text-white flex-shrink-0">
                      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                        <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"></path>
                        <circle cx="12" cy="7" r="4"></circle>
                      </svg>
                    </div>
                    <h2 class="text-gray-900 text-lg title-font font-medium">The Catalyzer</h2>
                  </div>
                  <div class="flex-grow">
                    <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.</p>
                    <a class="mt-3 text-indigo-500 inline-flex items-center">Learn More
                      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                        <path d="M5 12h14M12 5l7 7-7 7"></path>
                      </svg>
                    </a>
                  </div>
                </div>
              </div>
              <div class="p-4 md:w-1/3">
                <div class="flex rounded-lg h-full bg-gray-100 p-8 flex-col">
                  <div class="flex items-center mb-3">
                    <div class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full bg-indigo-500 text-white flex-shrink-0">
                      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                        <circle cx="6" cy="6" r="3"></circle>
                        <circle cx="6" cy="18" r="3"></circle>
                        <path d="M20 4L8.12 15.88M14.47 14.48L20 20M8.12 8.12L12 12"></path>
                      </svg>
                    </div>
                    <h2 class="text-gray-900 text-lg title-font font-medium">Neptune</h2>
                  </div>
                  <div class="flex-grow">
                    <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.</p>
                    <a class="mt-3 text-indigo-500 inline-flex items-center">Learn More
                      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                        <path d="M5 12h14M12 5l7 7-7 7"></path>
                      </svg>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
          <a class="text-gray-500"><svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z">

            </path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <rect width="20" height="20" x="2" y="2" rx="5" ry="5">

            </rect>
            <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37zm1.5-4.87h.01">

            </path>
            /svg>
          </a>
          <a class="ml-3 text-gray-500">
            <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" class="w-5 h-5" viewBox="0 0 24 24">
              <path stroke="none" d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z">

              </path>
              <circle cx="4" cy="4" r="2" stroke="none">

              </circle>
            </svg>
          </a>
        </span>
    </body>
    </html>
    ''')


def Maintenance(request):
    return HttpResponse('''

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Site Maintenance</title>
    </head>
    <body>
        <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
          <a  href ="http://127.0.0.1:8000/" class="mr-5 hover:text-gray-900">HOME</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact/Features" class="mr-5 hover:text-gray-900">FEATURES</a>
          <a  href ="http://127.0.0.1:8000/gallery" class="mr-5 hover:text-gray-900">GALERY</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us" class="mr-5 hover:text-gray-900">ABOUT US</a>
          <a href ="http://127.0.0.1:8000/gallery/about_us/contact" class="mr-5 hover:text-gray-900">CONTACT US</a>
        </nav>
        <hr>
    <style>
      body { text-align: center; padding: 150px; }
      h1 { font-size: 50px; }
      body { font: 20px Helvetica, sans-serif; color: #333; }
      article { display: block; text-align: left; width: 650px; margin: 0 auto; }
      a { color: #dc8100; text-decoration: none; }
      a:hover { color: #333; text-decoration: none; }
    </style>

    <article>
        <h1>We&rsquo;ll be back soon!</h1>
        <div>
            <p>Sorry for the inconvenience but we&rsquo;re performing some maintenance at the moment.
             If you need to you can always <a href="http://127.0.0.1:8000/gallery/about_us/contact">contact us</a>, 
             otherwise we&rsquo;ll be back online shortly!</p>
            <p>&mdash; The Sellton Team</p>
        </div>
    </article>
    </body>
    </html>
    ''')

