Title: Live Content

Description: Fetched live

Source: https://saeidehbakhshi.substack.com/p/how-to-build-a-simple-ai-moderated?r=1m4193&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true&triedRedirect=true&_src_ref=linkedin.com

---

<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8" />
        <meta name="norton-safeweb-site-verification" content="24usqpep0ejc5w6hod3dulxwciwp0djs6c6ufp96av3t4whuxovj72wfkdjxu82yacb7430qjm8adbd5ezlt4592dq4zrvadcn9j9n-0btgdzpiojfzno16-fnsnu7xd" />
        
        <link rel="preconnect" href="https://substackcdn.com" />
        

        
            <title data-rh="true">How to Build a Simple AI-Moderated Interviewer with a Custom GPT</title>
            
            <meta data-rh="true" name="theme-color" content="#FFFFFF"/><meta data-rh="true" property="og:type" content="article"/><meta data-rh="true" property="og:title" content="How to Build a Simple AI-Moderated Interviewer with a Custom GPT"/><meta data-rh="true" name="twitter:title" content="How to Build a Simple AI-Moderated Interviewer with a Custom GPT"/><meta data-rh="true" name="description" content="A practical DIY guide for building your own AI-moderated interviewer"/><meta data-rh="true" property="og:description" content="A practical DIY guide for building your own AI-moderated interviewer"/><meta data-rh="true" name="twitter:description" content="A practical DIY guide for building your own AI-moderated interviewer"/><meta data-rh="true" property="og:image" content="https://substackcdn.com/image/fetch/$s_!4srX!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73a65b1c-0bc0-4ff9-a418-d5bd8e239ab9_1655x524.png"/><meta data-rh="true" name="twitter:image" content="https://substackcdn.com/image/fetch/$s_!mIvU!,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsaeidehbakhshi.substack.com%2Fapi%2Fv1%2Fpost_preview%2F206239399%2Ftwitter.jpg%3Fversion%3D4"/><meta data-rh="true" name="twitter:card" content="summary_large_image"/><meta data-rh="true" property="article:modified_time" content="2026-07-09T04:49:09.110Z"/>
            
            
        

        

        <style>
          @layer legacy, tailwind, pencraftReset, pencraft;
        </style>

        
        <link rel="preload" as="style" href="https://substackcdn.com/bundle/theme/welcome.164d44f212a16669a0f2.css" />
        
        
        

        
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/679.38edce5a.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/92530.e798c7d0.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/69120.6ddde08f.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/38193.52728ca2.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/53861.80e5660a.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/47895.94566655.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/28116.a13b1c9d.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/13121.69b693eb.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/4799.9ce6e792.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/40697.f3f99703.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/37484.7bb9488c.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/87508.7222390d.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/41444.6f0dede2.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/70387.db956d59.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/12174.0731c0e4.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/85064.a66c9136.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/86696.c2ceb557.css" />
            
                <link rel="stylesheet" type="text/css" href="https://substackcdn.com/bundle/static/css/49127.813be60f.css" />
            
        

        
        
        
        
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0, viewport-fit=cover" />
        <meta name="author" content="Saeideh Bakhshi" />
        <meta property="og:url" content="https://saeidehbakhshi.substack.com/p/how-to-build-a-simple-ai-moderated" />
        
        
        <link rel="canonical" href="https://saeidehbakhshi.substack.com/p/how-to-build-a-simple-ai-moderated" />
        

        

        

        

        
            
                <link rel="shortcut icon" href="https://substackcdn.com/image/fetch/$s_!9JUC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Ffavicon.ico">
            
        
            
                <link rel="icon" type="image/png" sizes="16x16" href="https://substackcdn.com/image/fetch/$s_!400N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Ffavicon-16x16.png">
            
        
            
                <link rel="icon" type="image/png" sizes="32x32" href="https://substackcdn.com/image/fetch/$s_!KQWZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Ffavicon-32x32.png">
            
        
            
                <link rel="icon" type="image/png" sizes="48x48" href="https://substackcdn.com/image/fetch/$s_!8bTY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Ffavicon-48x48.png">
            
        
            
                <link rel="apple-touch-icon" sizes="57x57" href="https://substackcdn.com/image/fetch/$s_!LTCr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-57x57.png">
            
        
            
                <link rel="apple-touch-icon" sizes="60x60" href="https://substackcdn.com/image/fetch/$s_!A2fS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-60x60.png">
            
        
            
                <link rel="apple-touch-icon" sizes="72x72" href="https://substackcdn.com/image/fetch/$s_!EXMI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-72x72.png">
            
        
            
                <link rel="apple-touch-icon" sizes="76x76" href="https://substackcdn.com/image/fetch/$s_!Z2Ba!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-76x76.png">
            
        
            
                <link rel="apple-touch-icon" sizes="114x114" href="https://substackcdn.com/image/fetch/$s_!049V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-114x114.png">
            
        
            
                <link rel="apple-touch-icon" sizes="120x120" href="https://substackcdn.com/image/fetch/$s_!qL1l!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-120x120.png">
            
        
            
                <link rel="apple-touch-icon" sizes="144x144" href="https://substackcdn.com/image/fetch/$s_!qOmp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-144x144.png">
            
        
            
                <link rel="apple-touch-icon" sizes="152x152" href="https://substackcdn.com/image/fetch/$s_!NEdz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-152x152.png">
            
        
            
                <link rel="apple-touch-icon" sizes="167x167" href="https://substackcdn.com/image/fetch/$s_!isoN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-167x167.png">
            
        
            
                <link rel="apple-touch-icon" sizes="180x180" href="https://substackcdn.com/image/fetch/$s_!ADjz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-180x180.png">
            
        
            
                <link rel="apple-touch-icon" sizes="1024x1024" href="https://substackcdn.com/image/fetch/$s_!c-ow!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ddc98d-29f0-4e0f-852a-f8a9898f1284%2Fapple-touch-icon-1024x1024.png">
            
        
            
        
            
        
            
        

        

        
            <link rel="alternate" type="application/rss+xml" href="/feed" title="Research toolbox"/>
        

        
        
          <style>
            @font-face{font-family:'Spectral';font-style:italic;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCt-xNNww_2s0amA9M8on7mTNmnUHowCw.woff2) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:'Spectral';font-style:italic;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCt-xNNww_2s0amA9M8onXmTNmnUHowCw.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}@font-face{font-family:'Spectral';font-style:italic;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCt-xNNww_2s0amA9M8onTmTNmnUHowCw.woff2) format('woff2');unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:'Spectral';font-style:italic;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCt-xNNww_2s0amA9M8onrmTNmnUHo.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:'Spectral';font-style:normal;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCr-xNNww_2s0amA9M9knjsS_ulYHs.woff2) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:'Spectral';font-style:normal;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCr-xNNww_2s0amA9M2knjsS_ulYHs.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}@font-face{font-family:'Spectral';font-style:normal;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCr-xNNww_2s0amA9M3knjsS_ulYHs.woff2) format('woff2');unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:'Spectral';font-style:normal;font-weight:400;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCr-xNNww_2s0amA9M5knjsS_ul.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:'Spectral';font-style:normal;font-weight:600;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9vmtm3FafaPWnIIMrY.woff2) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:'Spectral';font-style:normal;font-weight:600;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9vmtm3OafaPWnIIMrY.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}@font-face{font-family:'Spectral';font-style:normal;font-weight:600;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9vmtm3PafaPWnIIMrY.woff2) format('woff2');unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:'Spectral';font-style:normal;font-weight:600;font-display:fallback;src:url(https://fonts.gstatic.com/s/spectral/v13/rnCs-xNNww_2s0amA9vmtm3BafaPWnII.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
            
          </style>
        
        
        
        

        <style data-pub-theme-prefix>:root{--color_theme_bg_pop:#FF6B00;--background_pop:#FF6B00;--cover_bg_color:#FFFFFF;--cover_bg_color_secondary:#f0f0f0;--background_pop_darken:#e66000;--print_on_pop:#ffffff;--color_theme_bg_pop_darken:#e66000;--color_theme_print_on_pop:#ffffff;--color_theme_bg_pop_20:rgba(255, 107, 0, 0.2);--color_theme_bg_pop_30:rgba(255, 107, 0, 0.3);--print_pop:#ff6b00;--color_theme_accent:#ff6b00;--cover_print_primary:#363737;--cover_print_secondary:#757575;--cover_print_tertiary:#b6b6b6;--cover_border_color:#ff6b00;--home_hero:feature-media;--home_posts:list;--home_show_top_posts:true;--web_bg_color:#FFFFFF;--background_contrast_1:#f0f0f0;--background_contrast_2:#dddddd;--background_contrast_3:#b7b7b7;--background_contrast_4:#929292;--background_contrast_5:#515151;--color_theme_bg_contrast_1:#f0f0f0;--color_theme_bg_contrast_2:#dddddd;--color_theme_bg_contrast_3:#b7b7b7;--color_theme_bg_contrast_4:#929292;--color_theme_bg_contrast_5:#515151;--color_theme_bg_elevated:#ffffff;--color_theme_bg_elevated_secondary:#f0f0f0;--color_theme_bg_elevated_tertiary:#dddddd;--color_theme_detail:#e6e6e6;--background_contrast_pop:rgba(255, 107, 0, 0.4);--color_theme_bg_contrast_pop:rgba(255, 107, 0, 0.4);--theme_bg_is_dark:0;--print_on_web_bg_color:#363737;--print_secondary_on_web_bg_color:#868787;--background_pop_rgb:255, 107, 0;--color_theme_bg_pop_rgb:255, 107, 0;--color_theme_accent_rgb:255, 107, 0;}</style>

        
            <link rel="stylesheet" href="https://substackcdn.com/bundle/theme/welcome.164d44f212a16669a0f2.css" />
        

        <style data-pub-theme-postfix></style>

        

        

        

        
    </head>

    <body class="">
        

        

        

        <div id="entry">
            <div class="pencraft pc-display-contents pc-reset coverTheme-PJLqY5"><div class="intro-popup"><div class="intro-popup-page"><div class="full-email-form"><div class="vertically-centered"><button tabindex="0" type="button" aria-label="Close" data-testid="close-welcome-modal" class="pencraft pc-reset pencraft closeWelcomeModal-KVUfKQ iconButton-mq_Et5 iconButtonBase-dJGHgN buttonBase-GK1x3M buttonStyle-r7yGCK size_md-gCDS3o priority_tertiary-rlke8z"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-x"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg></button><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!FjkG!,w_424,c_limit,f_webp,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 424w, https://substackcdn.com/image/fetch/$s_!FjkG!,w_848,c_limit,f_webp,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 848w, https://substackcdn.com/image/fetch/$s_!FjkG!,w_1272,c_limit,f_webp,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 1272w, https://substackcdn.com/image/fetch/$s_!FjkG!,w_1360,c_limit,f_webp,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 1360w" sizes="100vw"/><img src="https://substackcdn.com/image/fetch/$s_!FjkG!,w_1360,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png" sizes="100vw" alt srcset="https://substackcdn.com/image/fetch/$s_!FjkG!,w_424,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 424w, https://substackcdn.com/image/fetch/$s_!FjkG!,w_848,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 848w, https://substackcdn.com/image/fetch/$s_!FjkG!,w_1272,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 1272w, https://substackcdn.com/image/fetch/$s_!FjkG!,w_1360,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png 1360w" width="1360" loading="eager" style="height:min(35vh, 425px);" class="img-OACg1c publication-cover-photo pencraft pc-reset"/></picture><h1 class="publication-name with-cover balancedText-oQ__Kv">Research toolbox</h1><p class="publication-tagline with-cover verbose with-cover balancedText-oQ__Kv">Long time UX researcher, and a computational social scientist at OpenAI. I write about research, AI, UX measurement, and the evolving craft of understanding people in complex technological systems.</p><div class="publication-meta"><div class="pencraft pc-display-flex pc-gap-4 pc-reset pc-display-inline-flex">By Saeideh Bakhshi</div> · Over 2,000 subscribers</div><div style="width:100%;" class="pencraft pc-display-flex pc-justifyContent-center pc-reset"><div style="width:100%;max-width:380px;" class="pencraft pc-display-flex pc-flexDirection-column pc-gap-4 pc-reset"><div class="pencraft pc-display-flex pc-flexDirection-column pc-justifyContent-center pc-alignItems-center pc-reset emailFormContainer-TcAFa_"><div class="container-IpPqBD"><form action="/api/v1/free?nojs=true" method="post" novalidate class="form form-M5sC90"><input type="hidden" name="first_url" value/><input type="hidden" name="first_referrer" value/><input type="hidden" name="current_url"/><input type="hidden" name="current_referrer"/><input type="hidden" name="first_session_url" value/><input type="hidden" name="first_session_referrer" value/><input type="hidden" name="referral_code"/><input type="hidden" name="source" value="cover_page"/><input type="hidden" name="referring_pub_id"/><input type="hidden" name="additional_referring_pub_ids"/><div class="sideBySideWrap-vGXrwP"><div class="emailInputWrapper-QlA86j"><div class="pencraft pc-display-flex pc-minWidth-0 pc-position-relative pc-reset flex-auto-j3S2WA"><input name="email" placeholder="Type your email..." type="email" class="pencraft emailInput-OkIMeB emailInputOnWelcomePage-nqc9VK input-y4v6N4 inputText-pV_yWb"/></div></div><button tabindex="0" type="submit" disabled class="pencraft pc-reset pencraft rightButton primary subscribe-btn button-VFSdkv buttonOnWelcomePage-D2qOpe buttonBase-GK1x3M"><span class="button-text ">Subscribe</span></button></div><div id="error-container"></div></form></div></div><div class="pencraft pc-paddingLeft-0 pc-mobile-paddingLeft-16 pc-paddingRight-0 pc-mobile-paddingRight-16 pc-paddingTop-16 pc-reset tosText-yAQHNw"><div class="visibility-check"></div><label class="pencraft pc-display-flex pc-gap-12 pc-justifyContent-center pc-alignItems-center pc-reset tosCheckbox-XbLWCT"><div translated class="pencraft pc-reset color-secondary-ls1g8s align-center-y7ZD4w line-height-20-t4M0El font-text-qe4AeH size-13-hZTUKr weight-regular-mUq6Gb reset-IxiVJZ">By subscribing, you agree Substack's <a style="text-decoration:underline;" href="https://substack.com/tos" target="_blank" class="pencraft pc-reset reset-IxiVJZ">Terms of Use</a>, and acknowledge its <a style="text-decoration:underline;" href="https://substack.com/ccpa#personal-data-collected" target="_blank" class="pencraft pc-reset reset-IxiVJZ">Information Collection Notice</a> and <a style="text-decoration:underline;" href="https://substack.com/privacy" target="_blank" class="pencraft pc-reset reset-IxiVJZ">Privacy Policy</a>.</div></label></div></div></div><button tabindex="0" type="button" data-testid="maybeLater" class="pencraft pc-reset pencraft maybeLater-PlK9NK buttonBase-GK1x3M buttonText-X0uSmG buttonStyle-r7yGCK priority_quaternary-kpMibu size_md-gCDS3o">No thanks<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-right"><path d="m9 18 6-6-6-6"></path></svg></button></div></div></div></div></div>
        </div>

        
            <script src="https://js.sentry-cdn.com/6c2ff3e3828e4017b7faf7b63e24cdf8.min.js" crossorigin="anonymous"></script>
            <script>
                window.Sentry && window.Sentry.onLoad(function() {
                    window.Sentry.init({
                        environment: window._preloads.sentry_environment,
                        dsn: window._preloads.sentry_dsn,
                    })
                })
            </script>
        


        
        
        
        
        <script>window._preloads        = JSON.parse("{\"isEU\":false,\"language\":\"en\",\"country\":\"US\",\"leaderboardCountries\":[\"ES\",\"FR\",\"GB\",\"IT\",\"NL\"],\"enabledLeaderboardCountries\":[\"ES\",\"FR\",\"GB\",\"IT\",\"NL\"],\"userLocale\":{\"language\":\"en\",\"region\":\"US\",\"source\":\"default\"},\"base_url\":\"https://saeidehbakhshi.substack.com\",\"stripe_publishable_key\":\"pk_live_51QfnARLDSWi1i85FBpvw6YxfQHljOpWXw8IKi5qFWEzvW8HvoD8cqTulR9UWguYbYweLvA16P7LN6WZsGdZKrNkE00uGbFaOE3\",\"captcha_site_key\":\"6LeI15YsAAAAAPXyDcvuVqipba_jEFQCjz1PFQoz\",\"pub\":{\"apple_pay_disabled\":false,\"apex_domain\":null,\"author_id\":97605975,\"byline_images_enabled\":true,\"bylines_enabled\":true,\"chartable_token\":null,\"community_enabled\":true,\"copyright\":\"Saeideh Bakhshi\",\"cover_photo_url\":\"https://substack-post-media.s3.amazonaws.com/public/images/4b8faed2-9aa5-40fc-be31-46e83a63da5b_1280x800.png\",\"created_at\":\"2022-12-02T19:52:07.987Z\",\"custom_domain_optional\":false,\"custom_domain\":null,\"default_comment_sort\":\"best_first\",\"default_coupon\":null,\"default_group_coupon\":\"6f38b7a6\",\"default_show_guest_bios\":true,\"email_banner_url\":null,\"email_from_name\":\"Saeideh Bakhshi from Research Toolbox\",\"email_from\":null,\"embed_tracking_disabled\":false,\"explicit\":false,\"expose_paywall_content_to_search_engines\":true,\"fb_pixel_id\":null,\"fb_site_verification_token\":null,\"flagged_as_spam\":false,\"founding_subscription_benefits\":[\"One 30-minute Zoom chat each year, scheduled as availability allows\"],\"free_subscription_benefits\":[\"Free posts on research, AI, UX, and data-informed decision-making\"],\"ga_pixel_id\":null,\"google_site_verification_token\":null,\"google_tag_manager_token\":null,\"hero_image\":null,\"hero_text\":\"Long time UX researcher, and a computational social scientist at OpenAI. I write about research, AI, UX measurement, and the evolving craft of understanding people in complex technological systems.\",\"hide_intro_subtitle\":null,\"hide_intro_title\":null,\"hide_podcast_feed_link\":false,\"homepage_type\":\"newspaper\",\"id\":1223229,\"image_thumbnails_always_enabled\":false,\"invite_only\":false,\"hide_podcast_from_pub_listings\":false,\"language\":\"en\",\"logo_url_wide\":null,\"logo_url\":\"https://substackcdn.com/image/fetch/$s_!I7Qr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2dafa826-7cdf-484f-8e4d-8c8288ad4797_1254x1254.png\",\"minimum_group_size\":5,\"moderation_enabled\":true,\"name\":\"Research toolbox\",\"paid_subscription_benefits\":[\"Exclusive frameworks, guides, and playbooks\",\"Downloadable templates and practical research tools\",\"Full access to the Research Toolbox archive\"],\"parsely_pixel_id\":null,\"chartbeat_domain\":null,\"payments_state\":\"enabled\",\"paywall_free_trial_enabled\":true,\"podcast_art_url\":null,\"paid_podcast_episode_art_url\":null,\"podcast_byline\":null,\"podcast_description\":null,\"podcast_enabled\":false,\"podcast_feed_url\":null,\"podcast_title\":null,\"post_preview_limit\":null,\"primary_user_id\":97605975,\"require_clickthrough\":false,\"show_pub_podcast_tab\":false,\"show_recs_on_homepage\":true,\"subdomain\":\"saeidehbakhshi\",\"subscriber_invites\":0,\"support_email\":null,\"theme_var_background_pop\":\"#FF6B00\",\"theme_var_color_links\":false,\"theme_var_cover_bg_color\":null,\"trial_end_override\":null,\"twitter_pixel_id\":null,\"type\":\"newsletter\",\"post_reaction_faces_enabled\":true,\"is_personal_mode\":false,\"plans\":[{\"id\":\"monthly8usd\",\"object\":\"plan\",\"active\":true,\"aggregate_usage\":null,\"amount\":800,\"amount_decimal\":\"800\",\"billing_scheme\":\"per_unit\",\"created\":1779898059,\"currency\":\"usd\",\"interval\":\"month\",\"interval_count\":1,\"livemode\":true,\"metadata\":{\"substack\":\"yes\"},\"meter\":null,\"nickname\":\"$8 a month\",\"product\":\"prod_UavrO9Tsl9nLz1\",\"tiers_mode\":null,\"transform_usage\":null,\"trial_period_days\":null,\"usage_type\":\"licensed\",\"currency_options\":{\"aud\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":1200,\"unit_amount_decimal\":\"1200\"},\"brl\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":4200,\"unit_amount_decimal\":\"4200\"},\"cad\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":1200,\"unit_amount_decimal\":\"1200\"},\"chf\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":700,\"unit_amount_decimal\":\"700\"},\"dkk\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":5500,\"unit_amount_decimal\":\"5500\"},\"eur\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":800,\"unit_amount_decimal\":\"800\"},\"gbp\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":700,\"unit_amount_decimal\":\"700\"},\"mxn\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":14000,\"unit_amount_decimal\":\"14000\"},\"nok\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":8000,\"unit_amount_decimal\":\"8000\"},\"nzd\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":1500,\"unit_amount_decimal\":\"1500\"},\"pln\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":3100,\"unit_amount_decimal\":\"3100\"},\"sek\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":8000,\"unit_amount_decimal\":\"8000\"},\"usd\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":800,\"unit_amount_decimal\":\"800\"}}},{\"id\":\"yearly80usd\",\"object\":\"plan\",\"active\":true,\"aggregate_usage\":null,\"amount\":8000,\"amount_decimal\":\"8000\",\"billing_scheme\":\"per_unit\",\"created\":1779898060,\"currency\":\"usd\",\"interval\":\"year\",\"interval_count\":1,\"livemode\":true,\"metadata\":{\"substack\":\"yes\"},\"meter\":null,\"nickname\":\"$80 a year\",\"product\":\"prod_UavrnrdUYU75XK\",\"tiers_mode\":null,\"transform_usage\":null,\"trial_period_days\":null,\"usage_type\":\"licensed\",\"currency_options\":{\"aud\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":12000,\"unit_amount_decimal\":\"12000\"},\"brl\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":41500,\"unit_amount_decimal\":\"41500\"},\"cad\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":11500,\"unit_amount_decimal\":\"11500\"},\"chf\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":6500,\"unit_amount_decimal\":\"6500\"},\"dkk\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":52500,\"unit_amount_decimal\":\"52500\"},\"eur\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":7500,\"unit_amount_decimal\":\"7500\"},\"gbp\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":6500,\"unit_amount_decimal\":\"6500\"},\"mxn\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":140000,\"unit_amount_decimal\":\"140000\"},\"nok\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":79500,\"unit_amount_decimal\":\"79500\"},\"nzd\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":14500,\"unit_amount_decimal\":\"14500\"},\"pln\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":30500,\"unit_amount_decimal\":\"30500\"},\"sek\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":78000,\"unit_amount_decimal\":\"78000\"},\"usd\":{\"custom_unit_amount\":null,\"tax_behavior\":\"unspecified\",\"unit_amount\":8000,\"unit_amount_decimal\":\"8000\"}}},{\"id\":\"founding24000usd\",\"name\":\"founding24000usd\",\"nickname\":\"founding24000usd\",\"active\":true,\"amount\":24000,\"currency\":\"usd\",\"interval\":\"year\",\"interval_count\":1,\"metadata\":{\"substack\":\"yes\",\"founding\":\"yes\",\"no_coupons\":\"yes\",\"short_description\":\"Founding Member\",\"short_description_english\":\"Founding Member\",\"minimum\":\"8000\",\"minimum_local\":{\"aud\":11500,\"brl\":41000,\"cad\":11500,\"chf\":7000,\"dkk\":52500,\"eur\":7500,\"gbp\":6000,\"inr\":772500,\"jpy\":13500,\"mxn\":139500,\"nok\":77000,\"nzd\":14000,\"pln\":30500,\"sek\":78000,\"usd\":8000}},\"currency_options\":{\"aud\":{\"unit_amount\":34500,\"tax_behavior\":\"unspecified\"},\"brl\":{\"unit_amount\":122000,\"tax_behavior\":\"unspecified\"},\"cad\":{\"unit_amount\":34000,\"tax_behavior\":\"unspecified\"},\"chf\":{\"unit_amount\":20000,\"tax_behavior\":\"unspecified\"},\"dkk\":{\"unit_amount\":157500,\"tax_behavior\":\"unspecified\"},\"eur\":{\"unit_amount\":21500,\"tax_behavior\":\"unspecified\"},\"gbp\":{\"unit_amount\":18000,\"tax_behavior\":\"unspecified\"},\"inr\":{\"unit_amount\":2317500,\"tax_behavior\":\"unspecified\"},\"jpy\":{\"unit_amount\":39500,\"tax_behavior\":\"unspecified\"},\"mxn\":{\"unit_amount\":418000,\"tax_behavior\":\"unspecified\"},\"nok\":{\"unit_amount\":230500,\"tax_behavior\":\"unspecified\"},\"nzd\":{\"unit_amount\":41500,\"tax_behavior\":\"unspecified\"},\"pln\":{\"unit_amount\":91500,\"tax_behavior\":\"unspecified\"},\"sek\":{\"unit_amount\":233000,\"tax_behavior\":\"unspecified\"},\"usd\":{\"unit_amount\":24000,\"tax_behavior\":\"unspecified\"}}}],\"stripe_user_id\":\"acct_1TbjzVBd0T3tPQN4\",\"stripe_country\":\"US\",\"stripe_publishable_key\":\"pk_live_51TbjzVBd0T3tPQN412nM8dYEeS3oAyiwdkG5cuqbFwROy2TXXE9BCnKxp3iiuEMydMluqAY24e2XMAC90x9SrtgO00m1XRUTmh\",\"stripe_platform_account\":\"US\",\"automatic_tax_enabled\":false,\"author_name\":\"Saeideh Bakhshi\",\"author_handle\":\"researchtoolbox\",\"author_photo_url\":\"https://substackcdn.com/image/fetch/$s_!boEr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56e79fb2-75ce-4323-922c-7871a80a5b22_701x701.jpeg\",\"author_bio\":\"Mostly asking good questions, occasionally answering some\",\"has_custom_tos\":false,\"has_custom_privacy\":false,\"theme\":{\"background_pop_color\":null,\"web_bg_color\":\"#FFFFFF\",\"cover_bg_color\":null,\"publication_id\":1223229,\"color_links\":null,\"font_preset_heading\":null,\"font_preset_body\":null,\"font_family_headings\":null,\"font_family_body\":null,\"font_family_ui\":null,\"font_size_body_desktop\":null,\"print_secondary\":null,\"custom_css_web\":null,\"custom_css_email\":null,\"home_hero\":\"feature-media\",\"home_posts\":\"list\",\"home_show_top_posts\":true,\"hide_images_from_list\":false,\"home_hero_alignment\":\"left\",\"home_hero_show_podcast_links\":true,\"default_post_header_variant\":null,\"custom_header\":null,\"custom_footer\":null,\"social_media_links\":null,\"font_options\":null,\"section_template\":null,\"custom_subscribe\":null,\"design_template\":null,\"design_template_options\":null},\"threads_v2_settings\":{\"photo_replies_enabled\":true,\"first_thread_email_sent_at\":\"2023-03-22T23:08:06.325+00:00\",\"create_thread_minimum_role\":\"contributor\",\"activated_at\":\"2023-03-22T23:07:36.345+00:00\",\"reader_thread_notifications_enabled\":false,\"boost_free_subscriber_chat_preview_enabled\":true,\"push_suppression_enabled\":false},\"default_group_coupon_percent_off\":\"15.00\",\"default_group_coupon_include_founding\":false,\"pause_return_date\":null,\"has_posts\":true,\"has_recommendations\":true,\"first_post_date\":\"2023-01-04T20:43:46.049Z\",\"has_podcast\":false,\"has_free_podcast\":false,\"has_subscriber_only_podcast\":false,\"has_community_content\":true,\"rankingDetail\":\"Launched 4 years ago\",\"rankingDetailFreeIncluded\":\"Thousands of subscribers\",\"rankingDetailOrderOfMagnitude\":10,\"rankingDetailFreeIncludedOrderOfMagnitude\":1000,\"rankingDetailFreeSubscriberCount\":\"Over 2,000 subscribers\",\"rankingDetailByLanguage\":{\"ar\":{\"rankingDetail\":\"\u062A\u0645 \u0627\u0644\u0625\u0637\u0644\u0627\u0642 4 years ago\"},\"ca\":{\"rankingDetail\":\"S\u2019ha llan\u00E7at fa 4 anys\"},\"da\":{\"rankingDetail\":\"Lancering 4 \u00E5r\"},\"de\":{\"rankingDetail\":\"Vor vor 4 Jahren gelauncht\"},\"es\":{\"rankingDetail\":\"Lanzado hace 4 a\u00F1os\"},\"fr\":{\"rankingDetail\":\"Lanc\u00E9 il y a 4 ann\u00E9es\"},\"ja\":{\"rankingDetail\":\"\u958B\u59CB\u65E5 4\u5E74\u524D\"},\"nb\":{\"rankingDetail\":\"Lansert 4 \u00E5r\"},\"nl\":{\"rankingDetail\":\"Gelanceerd 4 jaar geleden\"},\"pl\":{\"rankingDetail\":\"Uruchomiono 4 lat temu\"},\"pt\":{\"rankingDetail\":\"Lan\u00E7ado 4 anos\"},\"pt-br\":{\"rankingDetail\":\"Lan\u00E7ado 4 anos\"},\"en-gb\":{\"rankingDetail\":\"Launched 4 years ago\"},\"it\":{\"rankingDetail\":\"Lanciato 4 anni\"},\"tr\":{\"rankingDetail\":\"4 y\u0131l ba\u015Flat\u0131ld\u0131\"},\"sv\":{\"rankingDetail\":\"Lanserad 4 \u00E5r sedan\"},\"fi\":{\"rankingDetail\":\"Launched 4 vuotta\"},\"is\":{\"rankingDetail\":\"Launched 4 \u00E1r\"},\"en\":{\"rankingDetail\":\"Launched 4 years ago\"}},\"freeSubscriberCount\":\"2,000\",\"freeSubscriberCountOrderOfMagnitude\":\"2.2K+\",\"author_bestseller_tier\":0,\"author_badge\":null,\"disable_monthly_subscriptions\":false,\"disable_annual_subscriptions\":false,\"hide_post_restacks\":false,\"notes_feed_enabled\":true,\"showIntroModule\":false,\"isPortraitLayout\":false,\"last_chat_post_at\":\"2023-05-03T16:15:21.371Z\",\"primary_profile_name\":\"Saeideh Bakhshi\",\"primary_profile_photo_url\":\"https://substackcdn.com/image/fetch/$s_!boEr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56e79fb2-75ce-4323-922c-7871a80a5b22_701x701.jpeg\",\"no_follow\":false,\"sponsorshipCampaigns\":{},\"paywall_chat\":\"free\",\"sections\":[],\"podcastTabInfo\":null,\"multipub_migration\":null,\"navigationBarItems\":[],\"has_active_perks\":false,\"contributors\":[{\"name\":\"Saeideh Bakhshi\",\"handle\":\"researchtoolbox\",\"role\":\"admin\",\"owner\":true,\"user_id\":97605975,\"photo_url\":\"https://substack-post-media.s3.amazonaws.com/public/images/56e79fb2-75ce-4323-922c-7871a80a5b22_701x701.jpeg\",\"bio\":\"Mostly asking good questions, occasionally answering some\",\"status\":{\"bestsellerTier\":null,\"subscriberTier\":null,\"leaderboard\":null,\"vip\":false,\"badge\":null,\"subscriber\":null}}],\"threads_v2_enabled\":true,\"viralGiftsConfig\":{\"id\":\"b9436179-e774-4da0-9305-0456ee035083\",\"publication_id\":1223229,\"enabled\":true,\"gifts_per_user\":5,\"gift_length_months\":1,\"send_extra_gifts\":true,\"message\":\"Writing on research, AI, product measurement, and the evolving craft of understanding people in complex systems.\",\"created_at\":\"2026-05-27T16:54:25.420716+00:00\",\"updated_at\":\"2026-05-27T16:54:25.420716+00:00\",\"days_til_invite\":14,\"send_emails\":true,\"show_link\":null},\"tier\":2,\"no_index\":false,\"can_set_google_site_verification\":true,\"can_have_sitemap\":true,\"iap_advanced_plans\":[{\"sku\":\"hDz5DhimVt4P5VkWWh\",\"publication_id\":\"1223229\",\"is_active\":true,\"price_base_units\":1100,\"currency_alpha3\":\"usd\",\"period\":\"month\",\"created_at\":\"2026-05-27T16:07:40.989Z\",\"updated_at\":\"2026-05-27T16:07:40.989Z\",\"id\":\"1163444\",\"payout_amount_base_units\":80,\"alternate_currencies\":{\"aud\":1600,\"brl\":6000,\"cad\":1600,\"chf\":900,\"dkk\":7500,\"eur\":1000,\"gbp\":900,\"mxn\":19500,\"nok\":10500,\"nzd\":1900,\"pln\":4100,\"sek\":10500},\"is_founding\":false,\"display_name\":\"Research toolbox (Monthly)\",\"display_price\":\"$11\"},{\"sku\":\"yntyYIEs107ESvxrZS\",\"publication_id\":\"1223229\",\"is_active\":true,\"price_base_units\":11000,\"currency_alpha3\":\"usd\",\"period\":\"year\",\"created_at\":\"2026-05-27T16:07:41.001Z\",\"updated_at\":\"2026-05-27T16:07:41.001Z\",\"id\":\"1163445\",\"payout_amount_base_units\":800,\"alternate_currencies\":{\"aud\":15500,\"brl\":55500,\"cad\":15500,\"chf\":9000,\"dkk\":71000,\"eur\":9500,\"gbp\":8500,\"mxn\":190500,\"nok\":102000,\"nzd\":19000,\"pln\":40500,\"sek\":102500},\"is_founding\":false,\"display_name\":\"Research toolbox (Yearly)\",\"display_price\":\"$110\"}],\"founding_plan_name_english\":\"Founding Member\",\"iap_founding_plan\":{\"base_plan_id\":\"founding24000usd\",\"name\":\"Founding Member\",\"minimum_amount\":11000,\"suggested_amount\":33000,\"currency_alpha3\":\"usd\",\"alternate_currencies\":{\"aud\":{\"minimum_amount\":16000,\"suggested_amount\":47500},\"brl\":{\"minimum_amount\":56000,\"suggested_amount\":167500},\"cad\":{\"minimum_amount\":15500,\"suggested_amount\":46500},\"chf\":{\"minimum_amount\":9000,\"suggested_amount\":27000},\"dkk\":{\"minimum_amount\":72500,\"suggested_amount\":216500},\"eur\":{\"minimum_amount\":10000,\"suggested_amount\":29000},\"gbp\":{\"minimum_amount\":8500,\"suggested_amount\":25000},\"inr\":{\"minimum_amount\":1062500,\"suggested_amount\":3186500},\"jpy\":{\"minimum_amount\":18000,\"suggested_amount\":54000},\"mxn\":{\"minimum_amount\":191500,\"suggested_amount\":574500},\"nok\":{\"minimum_amount\":106000,\"suggested_amount\":317000},\"nzd\":{\"minimum_amount\":19000,\"suggested_amount\":57000},\"pln\":{\"minimum_amount\":42000,\"suggested_amount\":125500},\"sek\":{\"minimum_amount\":107000,\"suggested_amount\":320500}}},\"base_url\":\"https://saeidehbakhshi.substack.com\",\"hostname\":\"saeidehbakhshi.substack.com\",\"is_on_substack\":false,\"spotify_podcast_settings\":null,\"unified_podcast_settings\":null,\"podcastPalette\":{\"DarkMuted\":{\"population\":72,\"rgb\":[73,153,137]},\"DarkVibrant\":{\"population\":6013,\"rgb\":[4,100,84]},\"LightMuted\":{\"population\":7,\"rgb\":[142,198,186]},\"LightVibrant\":{\"population\":3,\"rgb\":[166,214,206]},\"Muted\":{\"population\":6,\"rgb\":[92,164,156]},\"Vibrant\":{\"population\":5,\"rgb\":[76,164,146]}},\"pageThemes\":{\"podcast\":null},\"supports_ip_content_unlock\":false,\"appTheme\":{\"colors\":{\"accent\":{\"name\":\"#ff6b00\",\"primary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1},\"primary_hover\":{\"r\":232,\"g\":88,\"b\":0,\"a\":1},\"primary_elevated\":{\"r\":232,\"g\":88,\"b\":0,\"a\":1},\"secondary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.2},\"contrast\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"bg\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.2},\"bg_hover\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.3},\"dark\":{\"primary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1},\"primary_hover\":{\"r\":255,\"g\":136,\"b\":66,\"a\":1},\"primary_elevated\":{\"r\":255,\"g\":136,\"b\":66,\"a\":1},\"secondary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.2},\"contrast\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"bg\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.2},\"bg_hover\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.3}}},\"fg\":{\"primary\":{\"r\":0,\"g\":0,\"b\":0,\"a\":0.8},\"secondary\":{\"r\":0,\"g\":0,\"b\":0,\"a\":0.6},\"tertiary\":{\"r\":0,\"g\":0,\"b\":0,\"a\":0.4},\"accent\":{\"r\":210,\"g\":68,\"b\":0,\"a\":1},\"dark\":{\"primary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0.9},\"secondary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0.6},\"tertiary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0.4},\"accent\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1}}},\"bg\":{\"name\":\"#ffffff\",\"hue\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0},\"tint\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0},\"primary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"primary_hover\":{\"r\":250,\"g\":250,\"b\":250,\"a\":1},\"primary_elevated\":{\"r\":250,\"g\":250,\"b\":250,\"a\":1},\"secondary\":{\"r\":238,\"g\":238,\"b\":238,\"a\":1},\"secondary_elevated\":{\"r\":206.90096477355226,\"g\":206.90096477355175,\"b\":206.9009647735519,\"a\":1},\"tertiary\":{\"r\":219,\"g\":219,\"b\":219,\"a\":1},\"quaternary\":{\"r\":182,\"g\":182,\"b\":182,\"a\":1},\"dark\":{\"primary\":{\"r\":22,\"g\":23,\"b\":24,\"a\":1},\"primary_hover\":{\"r\":27,\"g\":28,\"b\":29,\"a\":1},\"primary_elevated\":{\"r\":27,\"g\":28,\"b\":29,\"a\":1},\"secondary\":{\"r\":35,\"g\":37,\"b\":37,\"a\":1},\"secondary_elevated\":{\"r\":41.35899397549579,\"g\":43.405356429195315,\"b\":43.40489285041963,\"a\":1},\"tertiary\":{\"r\":54,\"g\":55,\"b\":55,\"a\":1},\"quaternary\":{\"r\":90,\"g\":91,\"b\":91,\"a\":1}}}}},\"portalAppTheme\":{\"colors\":{\"accent\":{\"name\":\"#FF6B00\",\"primary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1},\"primary_hover\":{\"r\":230,\"g\":96,\"b\":0,\"a\":1},\"primary_elevated\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1},\"secondary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1},\"contrast\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"bg\":{\"r\":255,\"g\":103,\"b\":25,\"a\":0.2},\"bg_hover\":{\"r\":255,\"g\":103,\"b\":25,\"a\":0.3},\"dark\":{\"primary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1},\"primary_hover\":{\"r\":255,\"g\":136,\"b\":66,\"a\":1},\"primary_elevated\":{\"r\":255,\"g\":136,\"b\":66,\"a\":1},\"secondary\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.2},\"contrast\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"bg\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.2},\"bg_hover\":{\"r\":255,\"g\":107,\"b\":0,\"a\":0.3}}},\"fg\":{\"primary\":{\"r\":54,\"g\":55,\"b\":55,\"a\":1},\"secondary\":{\"r\":134,\"g\":135,\"b\":135,\"a\":1},\"tertiary\":{\"r\":146,\"g\":146,\"b\":146,\"a\":1},\"accent\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1},\"dark\":{\"primary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0.9},\"secondary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0.6},\"tertiary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":0.4},\"accent\":{\"r\":255,\"g\":107,\"b\":0,\"a\":1}}},\"bg\":{\"name\":\"#FFFFFF\",\"hue\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"tint\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"primary\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"primary_hover\":{\"r\":240,\"g\":240,\"b\":240,\"a\":1},\"primary_elevated\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"secondary\":{\"r\":240,\"g\":240,\"b\":240,\"a\":1},\"secondary_elevated\":{\"r\":240,\"g\":240,\"b\":240,\"a\":1},\"tertiary\":{\"r\":221,\"g\":221,\"b\":221,\"a\":1},\"quaternary\":{\"r\":183,\"g\":183,\"b\":183,\"a\":1},\"dark\":{\"primary\":{\"r\":22,\"g\":23,\"b\":24,\"a\":1},\"primary_hover\":{\"r\":27,\"g\":28,\"b\":29,\"a\":1},\"primary_elevated\":{\"r\":27,\"g\":28,\"b\":29,\"a\":1},\"secondary\":{\"r\":35,\"g\":37,\"b\":37,\"a\":1},\"secondary_elevated\":{\"r\":41.35899397549579,\"g\":43.405356429195315,\"b\":43.40489285041963,\"a\":1},\"tertiary\":{\"r\":54,\"g\":55,\"b\":55,\"a\":1},\"quaternary\":{\"r\":90,\"g\":91,\"b\":91,\"a\":1}}},\"wordmark_bg\":{\"r\":255,\"g\":255,\"b\":255,\"a\":1},\"is_dark\":false}},\"logoPalette\":{\"Vibrant\":{\"rgb\":[51,125,138],\"population\":25},\"DarkVibrant\":{\"rgb\":[12,100,116],\"population\":6},\"LightVibrant\":{\"rgb\":[244,249,252],\"population\":10},\"Muted\":{\"rgb\":[84,148,158],\"population\":3},\"DarkMuted\":{\"rgb\":[60,62,67],\"population\":9},\"LightMuted\":{\"rgb\":[186,209,215],\"population\":36}}},\"confirmedLogin\":false,\"hide_intro_popup\":false,\"block_auto_login\":false,\"domainInfo\":{\"isSubstack\":true,\"customDomain\":null},\"experimentFeatures\":{},\"experimentExposures\":{},\"siteConfigs\":{\"score_upsell_email\":\"control\",\"first_chat_email_enabled\":true,\"new_commenter_approval\":false,\"pub_update_opennode_api_key\":false,\"notes_video_max_duration_minutes\":15,\"show_content_label_age_gating_in_feed\":false,\"zendesk_automation_cancellations\":false,\"enable_saved_segments\":false,\"mfa_action_box_enabled\":false,\"publication_max_bylines\":35,\"no_contest_charge_disputes\":false,\"feed_posts_previously_seen_weight\":0.1,\"publication_tabs_reorder\":false,\"comp_expiry_email_new_copy\":\"NONE\",\"free_unlock_required\":false,\"enable_post_summarization\":false,\"live_stream_host_warning_message\":\"\",\"bitcoin_enabled\":false,\"minimum_ios_os_version\":\"17.0.0\",\"show_entire_square_image\":false,\"hide_subscriber_count\":false,\"fit_in_live_stream_player\":false,\"publication_author_display_override\":\"\",\"generate_pdf_tax_report\":false,\"hide_post_sidebar\":false,\"show_generic_post_importer\":false,\"enable_pledges_modal\":true,\"enable_podcast_bonus_video\":true,\"notes_weight_watch_video\":3,\"enable_react_dashboard\":false,\"enable_videos_page\":false,\"exempt_from_gtm_filter\":false,\"group_sections_and_podcasts_in_menu\":false,\"boost_optin_modal_enabled\":true,\"standards_and_enforcement_features_enabled\":false,\"pub_creation_captcha_behavior\":\"risky_pubs_or_rate_limit\",\"post_blogspot_importer\":false,\"notes_weight_short_item_boost\":0.15,\"enable_high_res_background_uploading\":false,\"pub_tts_override\":\"default\",\"disable_monthly_subscriptions\":false,\"skip_welcome_email\":false,\"chat_reader_thread_notification_default\":false,\"scheduled_pinned_posts\":false,\"disable_redirect_outbound_utm_params\":false,\"reader_gift_referrals_enabled\":true,\"dont_show_guest_byline\":false,\"like_comments_enabled\":true,\"enable_sponsorship_campaigns_advanced\":false,\"temporal_livestream_ended_draft\":true,\"enable_author_note_email_toggle\":false,\"enable_pangram_ai_detection\":true,\"fallback_to_archive_search_on_section_pages\":false,\"livekit_track_egress_custom_base_url\":\"http://livekit-egress-custom-recorder-participant-test.s3-website-us-east-1.amazonaws.com\",\"welcome_screen_blurb_override\":\"\",\"notes_weight_low_impression_boost\":0.3,\"like_posts_enabled\":true,\"twitter_player_card_enabled\":true,\"feed_promoted_user\":false,\"show_note_stats_for_all_notes\":false,\"section_specific_csv_imports_enabled\":false,\"disable_podcast_feed_description_cta\":false,\"bypass_profile_substack_logo_detection\":false,\"use_preloaded_player_sources\":false,\"list_pruning_enabled\":false,\"facebook_connect\":false,\"opt_in_to_sections_during_subscribe\":false,\"dpn_weight_share\":2,\"underlined_colored_links\":false,\"enable_efficient_digest_embed\":false,\"enable_aligned_images\":false,\"max_image_upload_mb\":64,\"thefp_paywall_weekly_pricing\":\"control\",\"threads_suggested_ios_version\":null,\"pledges_disabled\":false,\"threads_minimum_ios_version\":812,\"hide_podcast_email_setup_link\":false,\"subscribe_captcha_behavior\":\"default\",\"publication_ban_sample_rate\":0,\"custom_themes_substack_subscribe_modal\":false,\"ios_post_share_assets_screenshot_trigger\":\"control\",\"opt_in_to_sections_during_subscribe_include_main_pub_newsletter\":false,\"continue_support_cta_in_newsletter_emails\":false,\"bloomberg_syndication_enabled\":false,\"allow_document_freeze\":false,\"test_age_gate_user\":false,\"podcast_main_feed_is_firehose\":false,\"pub_app_incentive_gift\":\"\",\"no_embed_redirect\":false,\"read_tab_v2_experiment\":\"control\",\"customized_email_from_name_for_new_follow_emails\":\"treatment\",\"spotify_open_access_sandbox_mode\":false,\"disable_custom_nav_menu\":false,\"enable_livestream_name_cards\":false,\"fullstory_enabled\":false,\"chat_reply_poll_interval\":3,\"dpn_weight_follow_or_subscribe\":3,\"thefp_enable_email_upsell_banner\":false,\"force_pub_links_to_use_subdomain\":false,\"always_show_cookie_banner\":false,\"hide_media_download_option\":false,\"hide_post_restacks\":false,\"feed_item_source_debug_mode\":false,\"publication_homepage_title_display_override\":\"\",\"live_stream_founding_audience_enabled\":true,\"post_preview_highlight_byline\":false,\"4k_video\":false,\"enable_islands_section_intent_screen\":false,\"post_metering_enabled\":false,\"notifications_disabled\":\"\",\"cross_post_notification_threshold\":1000,\"facebook_connect_prod_app\":true,\"force_into_pymk_ranking\":false,\"minimum_android_version\":756,\"group_size_change_notification_email_enabled\":false,\"enable_transcription_translations\":false,\"unified_media_editor_modal\":true,\"use_og_image_as_twitter_image_for_post_previews\":false,\"always_use_podcast_channel_art_as_episode_art_in_rss\":false,\"seo_tier_override\":\"NONE\",\"editor_role_enabled\":false,\"no_follow_links\":false,\"publisher_api_enabled\":false,\"zendesk_support_priority\":\"default\",\"enable_post_clips_stats\":false,\"enable_subscriber_referrals_awards\":true,\"ios_profile_themes_feed_permalink_enabled\":false,\"use_publication_language_for_transcription\":false,\"show_substack_funded_gifts_tooltip\":true,\"disable_ai_transcription\":false,\"thread_permalink_preview_min_ios_version\":4192,\"per_pub_notification_settings\":false,\"live_stream_creation_enabled\":true,\"disable_card_element_in_europe\":false,\"web_growth_item_promotion_threshold\":0,\"bundle_subscribe_enabled\":false,\"enable_web_typing_indicators\":false,\"web_vitals_sample_rate\":0,\"allow_live_stream_auto_takedown\":\"true\",\"mobile_publication_attachments_enabled\":false,\"enable_posts_to_segments\":false,\"enable_design_templates_events_page\":false,\"ai_image_generation_enabled\":true,\"disable_personal_substack_initialization\":false,\"section_specific_welcome_pages\":false,\"local_payment_methods\":\"control\",\"publisher_api_cancel_comp\":false,\"posts_in_rss_feed\":20,\"publisher_dashboard_section_selector\":false,\"reader_surveys_platform_question_order\":\"36,1,4,2,3,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35\",\"login_guard_app_link_in_email\":true,\"community_moderators_enabled\":false,\"enable_custom_theme\":false,\"monthly_sub_is_one_off\":false,\"unread_notes_activity_digest\":\"control\",\"display_cookie_settings\":false,\"welcome_page_query_params\":false,\"enable_free_podcast_urls\":false,\"comp_expiry_emails_disabled\":false,\"enable_description_on_polls\":false,\"use_microlink_for_instagram_embeds\":false,\"free_signup_confirmation_behavior\":\"with_email_validation\",\"ios_post_stats_for_admins\":false,\"enable_design_templates\":false,\"use_livestream_post_media_composition\":true,\"section_specific_preambles\":false,\"pub_export_temp_disable\":false,\"show_menu_on_posts\":false,\"global_iap_plan_setup_countries\":\"\",\"ios_post_subscribe_web_routing\":true,\"enable_pangram_detection_settings\":false,\"freewalls_enabled_web\":false,\"app_onboarding_survey_email\":false,\"republishing_enabled\":false,\"app_mode\":false,\"show_phone_banner\":false,\"universal_post_translator\":\"treatment\",\"minimum_ios_version\":2200,\"enable_author_pages\":false,\"enable_decagon_chat\":true,\"first_month_upsell\":\"control\",\"enable_subscriber_tags\":false,\"new_user_checklist_enabled\":\"use_follower_count\",\"disable_high_res_recording\":false,\"latex_upgraded_inline\":false,\"anonymous_post_metering_enabled\":false,\"rss_verification_code\":\"\",\"notification_post_emails\":\"experiment\",\"notes_weight_follow\":3.8,\"chat_suppress_contributor_push_option_enabled\":false,\"media_feed_app_prepend_inbox_limit\":0,\"export_hooks_enabled\":false,\"audio_encoding_bitrate\":null,\"extra_seats_coupon_type\":false,\"post_subdomain_universal_links\":false,\"post_import_max_file_size\":26214400,\"feed_promoted_video_publication\":false,\"livekit_reconnect_slate_url\":\"https://mux-livestream-assets.s3.us-east-1.amazonaws.com/custom-disconnect-slate-tall.png\",\"exclude_from_pymk_suggestions\":false,\"publication_ranking_variant\":\"experiment\",\"disable_annual_subscriptions\":false,\"hack_jane_manchun_wong\":true,\"android_enable_auto_gain_control\":true,\"allow_coupons_on_upgrade\":false,\"test_au_age_gate_user\":false,\"pub_auto_moderation_enabled\":false,\"disable_live_stream_ai_trimming_by_default\":false,\"disable_deletion\":false,\"ios_default_coupon_enabled\":false,\"notes_weight_read_post\":5,\"notes_weight_reply\":3,\"livekit_egress_custom_base_url\":\"http://livekit-egress-custom-recorder.s3-website-us-east-1.amazonaws.com\",\"clip_focused_video_upload_flow\":false,\"live_stream_max_guest_users\":2,\"android_upgrade_alert_dialog_reincarnated\":true,\"enable_video_seo_data\":false,\"can_reimport_unsubscribed_users_with_2x_optin\":false,\"feed_posts_weight_subscribed\":0,\"founding_upgrade_during_gift_disabled\":false,\"thefp_enable_section_groups\":false,\"review_incoming_email\":\"default\",\"enable_founding_gifts\":false,\"enable_sponsorship_campaigns\":false,\"thread_permalink_preview_min_android_version\":2037,\"thefp_enable_embed_media_links\":false,\"sort_modal_search_results\":false,\"default_thumbnail_time\":10,\"pub_ranking_weight_retained_engagement\":1,\"load_test_unichat\":false,\"notes_read_post_baseline\":0,\"live_stream_head_alignment_guide\":false,\"free_press_combo_subscribe_flow_enabled\":false,\"enable_code_embed_toc\":false,\"enable_publication_tax_settings\":false,\"pub_ranking_weight_immediate_engagement\":0.5,\"gifts_from_substack_feature_available\":true,\"disable_ai_clips\":false,\"enable_elevenlabs_voiceovers\":false,\"thefp_enable_transcripts\":false,\"show_simple_post_editor\":false,\"instacart_integration_enabled\":false,\"enable_publication_podcasts_page\":false,\"ios_note_composer_settings_enabled\":false,\"enable_direct_message_request_bypass\":false,\"enable_apple_news_sync\":false,\"live_stream_in_trending_topic_overrides\":\"\",\"free_press_newsletter_promo_enabled\":false,\"account_based_post_metering_enabled\":false,\"disable_live_stream_reactions\":false,\"feed_posts_weight_negative\":2.5,\"instacart_partner_id\":\"\",\"clip_generation_3rd_party_vendor\":\"internal\",\"media_feed_prepend_inbox_limit\":35,\"welcome_page_no_opt_out\":false,\"notes_weight_negative\":1,\"notes_weight_click_see_more\":2,\"section_specific_postscripts\":false,\"edit_profile_theme_colors\":false,\"notes_weight_like\":2.4,\"disable_clipping_for_readers\":false,\"feed_posts_weight_share\":6,\"feed_posts_weight_reply\":3,\"feed_posts_weight_like\":1.5,\"enable_apple_podcast_delivery_self_serve_pem_files\":false,\"feed_posts_weight_save\":3,\"enable_press_kit_preview_modal\":false,\"dpn_weight_tap_clickbait_penalty\":0.5,\"feed_posts_weight_sign_up\":4,\"phone_verification_fallback_to_twilio\":false,\"live_stream_video_degradation_preference\":\"maintainFramerate\",\"enable_high_follower_dm\":true,\"pause_app_badges\":false,\"profile_feed_expanded_inventory\":false,\"livekit_mux_latency_mode\":\"low\",\"feed_juiced_user\":0,\"notes_click_see_more_baseline\":0.35,\"enable_polymarket_expandable_embeds\":true,\"publisher_dashboard_group_subs_sidebar\":false,\"android_onboarding_new_user_survey\":\"experiment\",\"use_advanced_commerce_api_for_iap\":false,\"skip_free_preview_language_in_podcast_notes\":false,\"larger_wordmark_on_publication_homepage\":false,\"enable_mobile_stats_for_admins\":false,\"ios_profile_themes_note_composer_enabled\":false,\"enable_persona_sandbox_environment\":false,\"notes_weight_click_item\":3,\"allowed_email_domains\":\"mozmail.com\",\"notes_weight_long_visit\":1,\"create_nav_item_from_tag\":false,\"bypass_single_unlock_token_limit\":false,\"notes_watch_video_baseline\":0.08,\"enable_code_embeds\":false,\"thefp_fourth_of_july_sale\":false,\"add_section_and_tag_metadata\":false,\"daily_promoted_notes_enabled\":true,\"enable_islands_cms\":false,\"enable_livestream_combined_stats\":false,\"redirect_to_pub_after_welcome_signup\":false,\"chartbeat_video_enabled\":false,\"enable_drip_campaigns\":false,\"enable_filtered_posts_on_homepage\":false,\"post_management_search_engine\":\"elasticsearch\",\"new_bestseller_leaderboard_feed_item_enabled\":false,\"feed_main_disabled\":false,\"enable_account_settings_revamp\":false,\"thefp_enable_fp_recirc_block\":false,\"enable_segments_ui_revamp\":false,\"top_search_variant\":\"control\",\"enable_debug_logs_ios\":false,\"show_pub_content_on_profile_for_pub_id\":0,\"show_pub_content_on_profile\":false,\"livekit_track_egress\":true,\"onboarding_suggestions_search\":\"experiment\",\"feed_tuner_enabled\":false,\"livekit_mux_latency_mode_rtmp\":\"low\",\"livekit_high_quality_egress\":false,\"dpn_weight_tap_bonus_subscribed\":0,\"iap_announcement_blog_url\":\"\",\"disable_code_embed_chrome\":false,\"enable_subscribers_comment_permission_on_paid_posts\":false,\"ios_livestream_feedback\":false,\"founding_plan_upgrade_warning\":false,\"dpn_weight_like\":3,\"dpn_weight_short_session\":1,\"ios_mediaplayer_reply_bar_v2\":false,\"enable_notification_email_batching\":true,\"notes_weight_follow_boost\":10,\"ios_hide_portal_tab_bar\":false,\"follow_upsell_rollout_percentage\":30,\"enable_high_res_recording_default\":true,\"gift_article_enabled\":false,\"live_stream_invite_ttl_seconds\":900000,\"include_founding_plans_coupon_option\":false,\"thefp_enable_cancellation_discount_offer\":false,\"dpn_weight_reply\":2,\"android_enable_edit_profile_theme\":false,\"dpn_weight_follow\":3,\"notes_weight_author_low_impression_boost\":0.2,\"disable_audio_enhancement\":false,\"pub_search_variant\":\"control\",\"ignore_video_in_notes_length_limit\":false,\"notes_weight_click_share\":3,\"substack_gtm_enabled\":false,\"allow_long_videos\":true,\"feed_posts_weight_long_click\":15,\"dpn_score_threshold\":0,\"enable_automation_filters\":false,\"dpn_weight_follow_bonus\":0.5,\"enable_subscriber_perks_new_types\":true,\"use_enhanced_video_embed_player\":true,\"thefp_forum_enabled\":false,\"regional_leaderboard_visible\":true,\"founding_upgrade_preview\":false,\"enable_viewing_all_livestream_viewers\":false,\"send_subscription_canceled_email\":false,\"enable_clip_prompt_variant_filtering\":true,\"chartbeat_enabled\":false,\"dpn_weight_disable\":10,\"dpn_ranking_enabled\":true,\"enable_custom_email_css\":false,\"dpn_model_variant\":\"experiment\",\"enable_apple_podcast_auto_publish\":false,\"linkedin_profile_search_enabled\":false,\"publication_has_own_app\":false,\"suggested_minimum_ios_version\":0,\"dpn_weight_open\":2.5,\"thebulwark_enable_footer_actions\":false,\"trending_topics_module_long_term_experiment\":\"control\",\"enable_adhoc_email_scheduling\":false,\"enable_suggested_searches\":true,\"enable_subscription_notification_email_batching\":true,\"a24_redemption_link\":\"\",\"design_templates_launch_phase\":\"off\",\"post_custom_email_from_name_enabled\":false,\"dpn_weight_tap\":2.5,\"ios_live_stream_auto_gain_enabled\":true,\"dpn_weight_restack\":2,\"dpn_weight_negative\":40,\"enable_publication_tts_player\":false,\"enable_group_direct_messages\":false,\"enable_notes_admins\":false,\"thefp_show_pub_app_callout_on_post\":false,\"search_ranker_variant\":\"experiment\",\"forced_featured_topic_id\":\"\",\"ios_audio_captions_disabled\":false,\"web_podcasts_tab\":false,\"related_posts_enabled\":false,\"search_retrieval_variant\":\"experiment\",\"ios_live_stream_pip_dismiss_v4\":\"control\",\"reply_rate_limit_max_distinct_users_daily\":110,\"mobile_user_attachments_enabled\":false,\"web_post_metering_enabled\":false,\"feed_weight_language_mismatch_penalty\":0.6,\"publisher_banner\":\"\",\"web_inline_publication_chat\":true,\"enable_transcript_speaker_labeling\":true,\"enable_sponsorship_profile\":false,\"reply_rate_limit_max_distinct_users_monthly\":600,\"desktop_live_stream_screen_share_audio_enabled\":false,\"mobile_subscribe_app_takeover_notes\":\"control\",\"automod_admin_hidden_comments_tab\":true,\"dpn_weight_long_session\":2,\"ios_onboarding_new_user_survey\":\"experiment\",\"video_clip_suggestions_enabled\":false,\"android_polymarket_embed_search\":false,\"translate_posts_on_standalone_sites\":false,\"audience_section_editor_help_link\":\"https://support.substack.com/hc/en-us/articles/50558240901268-How-do-I-add-audience-specific-content-to-a-post-on-Substack\",\"portal_ranking_variant\":\"control\",\"permalink_reply_ranking_variant\":\"experiment\",\"allow_feed_category_filtering\":false,\"enable_dynamic_content\":true,\"enable_subscribers_comment_permission\":true,\"mobile_subscribe_app_takeover_app_upsell\":\"experiment\",\"private_live_streaming_enabled\":true,\"read_and_listen_tabs_experiment\":\"control\",\"desktop_live_stream_safe_framing\":0.8},\"trackingTokens\":{\"fbPixelId\":null,\"gaPixelId\":null,\"twitterPixelId\":null,\"parselyPixelId\":null,\"googleTagManagerToken\":null,\"googleAnalytics4Token\":null,\"twitterPixelSignupEventId\":null,\"twitterPixelSubscribeEventId\":null},\"publicationSettings\":{\"block_ai_crawlers\":false,\"credit_token_enabled\":true,\"custom_tos_and_privacy\":false,\"did_identity\":null,\"disable_optimistic_bank_payments\":false,\"display_welcome_page_details\":true,\"payment_pledges_enabled\":true,\"enable_drop_caps\":false,\"enable_post_page_conversion\":true,\"enable_prev_next_nav\":false,\"enable_restacking\":true,\"founding_group_subscriptions_enabled\":false,\"gifts_from_substack_disabled\":false,\"google_analytics_4_token\":null,\"group_sections_and_podcasts_in_menu_enabled\":false,\"live_stream_homepage_visibility\":\"contributorsAndAdmins\",\"live_stream_homepage_style\":\"autoPlay\",\"live_stream_replay_enabled\":true,\"medium_length_description\":\"\",\"notes_feed_enabled\":true,\"paywall_unlock_tokens\":false,\"post_preview_crop_gravity\":\"center\",\"post_preview_radius\":\"xs\",\"reader_referrals_enabled\":false,\"reader_referrals_leaderboard_enabled\":false,\"seen_coming_soon_explainer\":false,\"seen_google_analytics_migration_modal\":false,\"local_currency_modal_seen\":true,\"local_payment_methods_modal_seen\":false,\"twitter_pixel_signup_event_id\":null,\"twitter_pixel_subscribe_event_id\":null,\"use_local_currency\":true,\"welcome_page_opt_out_text\":\"No thanks\",\"cookie_settings\":\"\",\"show_restacks_below_posts\":true,\"holiday_gifting_post_header\":true,\"homepage_message_text\":\"\",\"homepage_message_link\":\"\",\"about_us_author_ids\":\"\",\"archived_section_ids\":\"\",\"column_section_ids\":\"\",\"fp_primary_column_section_ids\":\"\",\"event_section_ids\":\"\",\"podcasts_metadata\":\"\",\"video_section_ids\":\"\",\"post_metering_enabled\":false,\"account_based_post_metering_enabled\":false,\"use_custom_theme\":false,\"reply_rules\":null,\"automatic_moderation_enabled\":true,\"auto_translate_enabled\":true,\"additional_post_languages_enabled\":false,\"high_res_recording_beta\":false},\"publicationUserSettings\":null,\"userSettings\":{\"user_id\":null,\"activity_likes_enabled\":true,\"dashboard_nav_refresh_enabled\":false,\"is_guest_post_enabled\":true,\"invite_friends_nux_dismissed_at\":null,\"suggestions_feed_item_last_shown_at\":null,\"last_notification_alert_shown_at\":null,\"disable_reply_hiding\":false,\"newest_seen_chat_item_published_at\":null,\"explicitContentEnabled\":false,\"contactMatchingEnabled\":false,\"messageRequestLevel\":\"everyone\",\"liveStreamAcceptableInviteLevel\":\"everyone\",\"liveStreamAcceptableChatLevel\":\"everyone\",\"creditTokensTreatmentExposed\":false,\"appBadgeIncludesChat\":false,\"autoPlayVideo\":true,\"autoAdvanceVideo\":true,\"smart_delivery_enabled\":false,\"chatbotTermsLastAcceptedAt\":null,\"has_seen_notes_post_app_upsell\":false,\"first_note_id\":null,\"show_concurrent_live_stream_viewers\":false,\"edit_profile_feed_item_dismissed_at\":null,\"mobile_permalink_app_upsell_seen_at\":null,\"new_user_checklist_enabled\":false,\"has_seen_youtube_shorts_auto_publish_announcement\":false,\"has_seen_publish_youtube_connect_upsell\":false,\"notificationQualityFilterEnabled\":true,\"hasSeenOnboardingNewslettersScreen\":false,\"bestsellerBadgeEnabled\":true,\"hasSelfIdentifiedAsCreator\":false,\"autoTranslateEnabled\":true,\"autoTranslateBlocklist\":[],\"fineTuneFeedItemSeenAt\":null,\"fineTuneFeedItemDismissedAt\":null,\"aiGeneratedTextMode\":\"show\"},\"subscriberCountDetails\":\"thousands of subscribers\",\"mux_env_key\":\"u42pci814i6011qg3segrcpp9\",\"persona_environment_id\":\"env_o1Lbk4JhpY4PmvNkwaBdYwe5Fzkt\",\"sentry_environment\":\"production\",\"launchWelcomePage\":false,\"pendingInviteForActiveLiveStream\":null,\"isEligibleForLiveStreamCreation\":true,\"webviewPlatform\":null,\"postMetaData\":{\"id\":206239399,\"social_title\":null,\"title\":\"How to Build a Simple AI-Moderated Interviewer with a Custom GPT\",\"cover_image\":\"https://substackcdn.com/image/fetch/$s_!4srX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73a65b1c-0bc0-4ff9-a418-d5bd8e239ab9_1655x524.png\",\"type\":\"newsletter\",\"comment_count\":0,\"search_engine_description\":null,\"post_paywall_content_for_google\":false,\"slug\":\"how-to-build-a-simple-ai-moderated\",\"description\":\"A practical DIY guide for building your own AI-moderated interviewer\",\"audience\":\"only_paid\",\"publication_id\":1223229,\"post_date\":\"2026-07-09T04:47:57.869Z\",\"updated_at\":\"2026-07-09T04:49:09.110Z\",\"podcast_art_url\":null,\"reaction_count\":8},\"welcomePageData\":{\"blurbs\":[]},\"activeLiveStream\":null,\"freeTrialCoupon\":{\"id\":\"5af50469\",\"trial_period_days\":7},\"defaultCoupon\":null,\"isChatActive\":false,\"features\":{},\"browser\":{},\"showCookieBanner\":false,\"disabledCookies\":[],\"dd_env\":\"prod\",\"dd_ti\":true,\"mainBundleCSS\":[\"https://substackcdn.com/bundle/theme/main.a6f8054e69b981af1cb6.css\"]}")</script>
        <script>window._analyticsConfig = JSON.parse("{\"properties\":{\"subdomain\":\"saeidehbakhshi\",\"publication_id\":1223229,\"has_plans\":true,\"pub_community_enabled\":true,\"is_personal_publication\":false,\"is_subscribed\":false,\"is_free_subscribed\":false,\"is_author\":false,\"is_contributor\":false,\"is_admin\":false,\"is_founding\":false},\"adwordsAccountId\":\"AW-316245675\",\"adwordsEventSendTo\":\"Tf76CKqcyL4DEKuN5pYB\"}")</script>
        <script>window._src_ref = "https://linkedin.com/"</script>

        
        
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/71142.a4448cfa.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/47702.9a8f204d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/21080.a98572a1.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/32800.4e006403.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/2472.e47010b9.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/36479.64b00f26.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/78444.18ae49a8.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/2259.ae3b832d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/94409.df3958ee.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/75659.853e855c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/55825.5d058913.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/22618.ebbb25a2.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/36471.4e222ef9.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/11422.2b1d1d41.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/46519.8b782b3e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/679.f41df32c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/6904.1b23063e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/18725.3227804d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/92530.5b035112.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/12490.231d70dc.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/19408.dd38b077.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/3924.45d8357a.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/65458.24ce94fa.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/54911.25fa36bc.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/82171.b00de01b.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/99204.1b3701ae.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/38193.6c7c8b21.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/67990.91ae3849.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/26116.2d05732f.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/21978.962e66c0.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/40367.1144b338.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/10285.08b722e0.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/27467.6be1f44c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/53861.a46cfad3.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/17817.0df6f097.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/82282.a611ad7c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/59733.d8bb013b.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/29751.dad3ed7e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/welcome.138cae7d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/93367.7b1ccfdf.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/54770.8bc824ea.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/11796.3123be68.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/19387.2c661b47.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/2828.75d8da34.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/68875.c2c8ba13.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/8453.4d330054.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/47895.ed134bab.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/42517.35d0ef57.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/17135.074a2fbf.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/29822.c7f323f2.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/52412.a56639f4.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/64338.7e68cbd2.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/46929.700d5c5f.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/76630.b98a68c7.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/29429.41fe24a4.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/71534.80c1652d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/44469.23d64c33.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/81235.17cd77f4.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/28116.111c561e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/64461.dbf2c1b4.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/7760.09cbe6be.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/77604.0d4280e8.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/95815.864f5124.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/34330.f3b0ee15.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/62174.98af3e22.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/56787.56021b3e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/89737.f89e8547.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/13121.ae995e47.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/91982.3fbdf05c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/56654.2c9e3943.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/4799.a0dbb75b.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/34293.c8a5626c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/50898.84d04b7e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/90375.c927f9aa.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/83741.8b805a51.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/36630.fc0a6dfb.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/40697.6cda5627.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/64829.dac39050.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/79796.331bc680.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/10174.0685dee5.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/29177.81923662.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/95198.c2da2d6d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/29075.2fc3cd7d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/32517.d990b263.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/67395.c7d99717.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/37484.a1a08e81.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/4446.17ba52b5.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/52303.2e3db4e8.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/79373.c6f29417.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/18191.6914911a.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/58191.3e44eb9c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/74282.9094f68e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/93975.08e5f72b.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/33501.1cdb8b8a.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/72835.7d36bd23.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/21189.9bbf9d5d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/101.fa5ef0c6.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/7554.bffbf322.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/87508.10859d83.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/71199.baa1eba2.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/56256.a821c8bd.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/53164.b46a4286.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/34935.d6e83828.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/41444.8b00d619.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/70387.41f40a26.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/2102.74c44205.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/74584.b7f6a95e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/17296.bd5d325f.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/15549.0fad0aa7.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/12174.4cc2b0ee.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/7987.92b44fff.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/26132.4a5709f4.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/26136.0b3cc48a.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/85229.766ac118.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/85064.15fe34ab.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/31764.85d06ccc.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/68078.97a46600.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/81488.8cf26591.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/73672.0a7a3f0c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/99206.57920813.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/3663.dfecf0bf.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/41170.b844abfb.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/71362.0e21f015.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/11485.7f51cd56.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/86696.cb65336a.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/55721.ad92fbe3.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/49127.1c570aa9.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/59428.729d76b2.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/53173.b7a814e0.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/95574.719349d1.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/45181.894ef382.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/86870.71f57af6.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/17405.3a7f8805.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/82725.4d98a0f9.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/57051.4ba6c4f3.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/93977.28418dc2.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/24548.e250abed.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/19104.fa30f1a7.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/84756.bbf84cf9.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/56579.6d44a757.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/72659.92365d3a.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/56572.abeb2e11.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/87906.ddf30381.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/78191.5928727f.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/46124.e655949e.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/53149.c07b0c2c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/22306.88299e5b.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/80821.1cb0c5b5.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/91342.849053ee.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/19714.d08720c6.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/44014.f57d8fb8.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/90640.18cba16f.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/12.837dd6e4.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/38815.e913af34.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/57681.a2e543cb.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/91261.97d6ab17.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/53754.266b850d.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/30086.48489b14.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/48050.40ef563c.js" charset="utf-8"></script>
            
                <script defer type="module" src="https://substackcdn.com/bundle/static/js/lib-router.700d0377.js" charset="utf-8"></script>
            
        
        <script nomodule>
            (function() {
                var message = 'Your browser does not support modern JavaScript modules. Please upgrade your browser for the best experience.';
                var warningDiv = document.createElement('div');
                warningDiv.style.color = 'red';
                warningDiv.style.padding = '10px';
                warningDiv.style.margin = '10px 0';
                warningDiv.style.border = '1px solid red';
                warningDiv.style.backgroundColor = 'lightyellow';
                warningDiv.innerText = message;
                document.body.prepend(warningDiv);
            })();
        </script>

        
            <!-- Datadog Analytics -->
            <script>
              (function(h,o,u,n,d) {
                h=h[d]=h[d]||{q:[],onReady:function(c){h.q.push(c)}}
                d=o.createElement(u);d.async=1;d.src=n
                n=o.getElementsByTagName(u)[0];n.parentNode.insertBefore(d,n)
              })(window,document,'script','https://www.datadoghq-browser-agent.com/us1/v5/datadog-rum.js','DD_RUM')
              window.DD_RUM.onReady(function() {
                window.DD_RUM.init({
                  clientToken: 'puba71073f072643721169b68f352438710',
                  applicationId: '2e321b35-c76b-4073-8d04-cc9a10461793',
                  site: 'datadoghq.com',
                  service: 'web',
                  env: window._preloads.dd_env,
                  version: '85cc2c095f05f1fe85a72bdb3bf30befcb7b8683',
                  sessionSampleRate: 1,
                  sessionReplaySampleRate: 10,
                  trackUserInteractions: window._preloads.dd_ti,
                  trackResources: true,
                  trackLongTasks: true,
                  defaultPrivacyLevel: 'mask-user-input',
                  allowedTracingUrls: [/https?:\/\/(.+\/.)?substack(cdn)?\.com/]
                });
              })
            </script>
            <!-- End Datadog Analytics -->

            <!-- Cloudflare Web Analytics -->
            <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "216309cffb464db4b0e02daf0b8e8060"}'></script>
            <!-- End Cloudflare Web Analytics -->
        

        <!-- Fallback tracking pixels -->
        

        

        <noscript>
    <style>
        #nojs-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            padding: 16px 16px 16px 32px;
            width: 100%;
            box-sizing: border-box;
            background: red;
            color: white;
            font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
            font-size: 13px;
            line-height: 13px;
        }
        #nojs-banner a {
            color: inherit;
            text-decoration: underline;
        }
    </style>

    <div id="nojs-banner">
        This site requires JavaScript to run correctly. Please <a href="https://enable-javascript.com/" target="_blank">turn on JavaScript</a> or unblock scripts
    </div>
</noscript>


        

        

        
        
    <script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'a1f71e383ae651ac',t:'MTc4NDc3MjMwNA=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>


