<!DOCTYPE html>
<!-- saved from url=(0094)https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/light-0cfd1fd8509e.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/dark-d782f59290e2.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-f9fbc4b99a77.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-cff1c9b27b1a.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-70097f75aec1.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-c2f0d49bdcd9.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-4747d7bc0bc4.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-d3f6a61c91c8.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-a188d53f44bb.css">

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/primer-primitives-953961b66e63.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/primer-4430d3c2c150.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/global-47b8b2ca21ae.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/github-e72829f5538b.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/repository-d031bcc14e1b.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/code-9e1913b328be.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["alive_longer_retries","bypass_copilot_indexing_quota","copilot_new_references_ui","copilot_beta_features_opt_in","copilot_chat_retry_on_error","copilot_chat_persist_submitted_input","copilot_conversational_ux_history_refs","copilot_editor_upsells","copilot_free_limited_user","copilot_implicit_context","copilot_no_floating_button","copilot_smell_icebreaker_ux","experimentation_azure_variant_endpoint","failbot_handle_non_errors","geojson_azure_maps","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","hovercard_accessibility","issues_react_new_timeline","issues_react_avatar_refactor","issues_react_remove_placeholders","issues_react_blur_item_picker_on_close","issues_react_use_react_router_in_index","marketing_pages_search_explore_provider","react_keyboard_shortcuts_dialog","remove_child_patch","report_hydro_web_vitals","sample_network_conn_type","site_metered_billing_update","site_copilot_free","lifecycle_label_name_updates"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/wp-runtime-0378f971b53c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-9da652f58479.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_arianotify-polyfill_ariaNotify-polyfill_js-node_modules_github_mi-3abb8f-d7e6bc799724.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_failbot_failbot_ts-c551691a8183.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/environment-7b93e0f0c8ff.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_primer_behaviors_dist_esm_index_mjs-ea2a5d75d580.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-f690fd9ae3d5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_relative-time-element_dist_index_js-f6da4b3fa34c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-8e9f78-a74b4e0a8a6b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_text-expander-element_dist_index_js-78748950cb0c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-b5f1d7-a1760ffda83d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_markdown-toolbar-element_dist_index_js-ceef33f593fa.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-c44a69-c6d035fa8dc8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/github-elements-f991cfab5105.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/element-registry-d283cbab281e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-bb80ec-7f43298e364b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_lit-html_lit-html_js-be8cb88f481b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_morphdom_dist_morphdom-e-7c534c-a4a1922eb55f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-e3cbe28f1638.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-6cf3320416b8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_color-convert_index_js-e3180fe3bcb3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-69cfcc-833249ee3034.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_updatable-content_updatable-content_ts-863ef5872a03.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-900dde-917d4bda1f1a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/app_assets_modules_github_sticky-scroll-into-view_ts-7cbef09a422c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6-b41aeef03499.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-fb43816ab83c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/behaviors-a6abce982f3f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-f6223d90c7ba.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/notifications-global-cfcd9f4f0f23.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-96453a51f920.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-70450e-eecf0d50276f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/app_assets_modules_github_ref-selector_ts-842c74d2eab4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/codespaces-a493a4b9528f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-3eebbd-0763620ad7bf.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-e161aa-9d41fb1b6c9e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_remote--3c9c82-7238cfcdaa51.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/repositories-f3093651fb0e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-26cce2010167.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/code-menu-b5f092ec4b30.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/primer-react-753dc87b1e29.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/react-core-accb67f1350f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/react-lib-2131e17288a8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/octicons-react-45c3a19dd792.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_tanstack_query-core_build_modern_queryClient_js-e6f07a7e80b7.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-37e3d5-92730c05e718.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-e7dcdd-f7cc96ebae76.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-55fea94174bf.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/notifications-subscriptions-menu-51601778bd8d.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/primer-react.797c8ec006b327590422.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/notifications-subscriptions-menu.1bcff9205c241e99cff2.module.css">

  












  



  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  




      



        


  <meta http-equiv="x-pjax-version" content="5fff12adca0aaccac6e7cb955f5d2a759fadf460258f88f597531bdb75eb5aeb" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="ace39c3b6632770952207593607e6e0be0db363435a8b877b1f96abe6430f345" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="137747501b000c3c7ab6b8b92f1ded64f18d692f67bb1c163ffcea3636000502" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="7c097e7364773a7cbb9eb0b782ca541e1a2ac4fb1ef35cf49ecbc9e198f89bb3" data-turbo-track="reload">

  

      
  

  



      


    


  

  

  
  
  




  
  

  

  <style data-styled="active" data-styled-version="5.3.11"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/commits.1f3a5854808e827fcb0d.module.css"><script type="application/json" id="client-env">{"locale":"en","featureFlags":["alive_longer_retries","bypass_copilot_indexing_quota","copilot_new_references_ui","copilot_beta_features_opt_in","copilot_chat_retry_on_error","copilot_chat_persist_submitted_input","copilot_conversational_ux_history_refs","copilot_editor_upsells","copilot_free_limited_user","copilot_implicit_context","copilot_no_floating_button","copilot_smell_icebreaker_ux","experimentation_azure_variant_endpoint","failbot_handle_non_errors","geojson_azure_maps","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","hovercard_accessibility","issues_react_new_timeline","issues_react_avatar_refactor","issues_react_remove_placeholders","issues_react_blur_item_picker_on_close","issues_react_use_react_router_in_index","marketing_pages_search_explore_provider","react_keyboard_shortcuts_dialog","remove_child_patch","sample_network_conn_type","site_metered_billing_update","site_copilot_free","lifecycle_label_name_updates"]}</script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_dompurify_dist_purify_js-b89b98661809.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_react-relay_index_js-c5b7ce0827d5.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_lodash-es__Stack_js-node_modules_lodash-es__Uint8Array_js-node_modules_l-4faaa6-10d8eea337ce.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_date-fns_format_mjs-6e4d0f904632.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_date-fns_addWeeks_mjs-node_modules_date-fns_addYears_mjs-node_modules_da-827f4f-cf37cd06c24f.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_hotkey_dist_index_js-node_modules_primer_live-region-element_dist-ee65d7-b5a52b9eaa01.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_focus-visible_dist_focus-visible_js-node_modules_fzy_js_index_js-node_mo-c4d1d6-a009f6007b3c.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_date-fns_getDaysInMonth_mjs-node_modules_date-fns_isAfter_mjs-node_modul-49f526-6d4bedc5c754.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_lodash-es__baseIsEqual_js-8929eb9718d5.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_react-relay_hooks_js-node_modules_github_combobox-nav_dist_index_js-node-6d672f-6315950b19a4.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_hydro-analytics-fa0c26-b5ce76989c0a.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_aria-live_aria-live_ts-ui_packages_promise-with-resolvers-polyfill_promise-with-r-014121-a7926fdcecf7.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_paths_index_ts-4e4d706da555.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_ui-commands_ui-commands_ts-df3b47d86af0.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_list-view_src_ListItem_ListItem_tsx-ui_packages_list-view_src_ListItem_Title_tsx--68e5b9-a51927b092e0.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_date-picker_date-picker_ts-ui_packages_github-avatar_GitHubAvatar_tsx-b55eae95552d.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_item-picker_constants_labels_ts-ui_packages_item-picker_constants_values_ts-ui_pa-163a9a-6273f6ba9f14.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_item-picker_components_RepositoryPicker_tsx-b520a2bf2450.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_use-safe-async-callback_use-safe-async-callback_ts-ui_packages_copy-to-clipboard_-4c1096-9bd5b6266162.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_issue-create_dialog_CreateIssueDialogEntry_tsx-502d10cafe95.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_ref-selector_RefSelector_tsx-9445f4afb2bc.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_commenting_constants_values_ts-ui_packages_use-analytics_use-analytics_ts-ui_pack-af4212-eb918766c747.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_code-view-shared_utilities_web-worker_ts-ui_packages_code-view-shared_worker-jobs-cdcae1-f0dc8f3ae3e0.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/commits-252a5fb0bbd7.js.download"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><script type="application/javascript" src="./createmain_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_hotkey_dist_index_js-524e40420665.js.download"></script><script type="application/javascript" src="./createmain_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_remote-form_dist_-8c3668-4ebea233dc11.js.download"></script><script type="application/javascript" src="./createmain_files/ui_packages_form-utils_form-utils_ts-ui_packages_input-navigation-behavior_input-navigation-b-a97423-0ee33bdc7197.js.download"></script><script type="application/javascript" src="./createmain_files/issues-49a49680995d.js.download"></script><script type="application/javascript" src="./createmain_files/structured-issues-eb321c77cee9.js.download"></script><link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/staff-0aa284f91bc2.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/devtools-ed3c56d5f6b2.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/repos-overview.9cc263aa0716ce801059.module.css"><script type="application/javascript" src="./createmain_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-843b41414e0e.js.download"></script><script type="application/javascript" src="./createmain_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-9002b0-881da98a8b00.js.download"></script><script type="application/javascript" src="./createmain_files/ui_packages_code-view-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_hooks-503c34-7dfba50d2c16.js.download"></script><script type="application/javascript" src="./createmain_files/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-56ee79-b20e64ad06f9.js.download"></script><script type="application/javascript" src="./createmain_files/repos-overview-e21499fb8264.js.download"></script><link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/react-code-view.6b587a69b593e23c3657.module.css"><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-9002b0-881da98a8b00.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_code-view-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_hooks-503c34-7dfba50d2c16.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/ui_packages_document-metadata_document-metadata_ts-ui_packages_repos-file-tree-view_repos-fil-5db355-d0627efd6544.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/app_assets_modules_github_blob-anchor_ts-ui_packages_code-nav_code-nav_ts-ui_packages_filter--8253c1-f38cdfca9137.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/react-code-view-46a8d3dce54e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-843b41414e0e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_github_details-dialog-elem-308dee-23f281d9acce.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_scroll-anchoring_dist_scroll-anchoring_esm_js-node_modules_github_cataly-db906b-3eeea7fa8b27.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/app_assets_modules_github_diffs_blob-lines_ts-app_assets_modules_github_diffs_linkable-line-n-b8c0ea-be4e711b7e28.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/diffs-d41e3f1a4f7b.js.download"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/primer-react-753dc87b1e29.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/react-core-accb67f1350f.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/react-lib-2131e17288a8.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/octicons-react-45c3a19dd792.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_tanstack_query-core_build_modern_queryClient_js-e6f07a7e80b7.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-37e3d5-92730c05e718.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-e7dcdd-f7cc96ebae76.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-55fea94174bf.js.download"></script><link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/primer-react.797c8ec006b327590422.module.css"><title>Commits · AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline · GitHub</title><meta name="route-pattern" content="/:user_id/:repository/commits(/*name)" data-turbo-transient=""><meta name="route-controller" content="commits" data-turbo-transient=""><meta name="route-action" content="show" data-turbo-transient=""><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="F5C8:6FE24:5F6CEC:746DA4:67670A9C" data-pjax-transient="true"><meta name="html-safe-nonce" content="c3d2a21f3e575862bb9fbae9424cb60cb4ddd2a347e2f4b4f2bb4a7ac67c71ea" data-pjax-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9BYXJ0aGlWZWxwdWxhL0NoYXQtd2l0aC1QREYtVXNpbmctUkFHLVBpcGVsaW5lL2NvbW1pdHMiLCJyZXF1ZXN0X2lkIjoiRjVDODo2RkUyNDo1RjZDRUM6NzQ2REE0OjY3NjcwQTlDIiwidmlzaXRvcl9pZCI6Ijc4OTkxMTYzMzQyNTU4ODIxMTMiLCJyZWdpb25fZWRnZSI6ImNlbnRyYWxpbmRpYSIsInJlZ2lvbl9yZW5kZXIiOiJjZW50cmFsaW5kaWEifQ==" data-pjax-transient="true"><meta name="visitor-hmac" content="686b54d718551716f70dcf6066ec46de62a625d143f03b489f09e2ce69873ee8" data-pjax-transient="true"><meta name="hovercard-subject-tag" content="repository:906725444" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,commit-list,copilot" data-turbo-transient="true"><meta name="selected-link" value="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/commits/show" data-turbo-transient="true"><meta name="user-login" content=""><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta name="go-import" content="github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline git https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline.git"><meta name="octolytics-dimension-user_id" content="149761483"><meta name="octolytics-dimension-user_login" content="AarthiVelpula"><meta name="octolytics-dimension-repository_id" content="906725444"><meta name="octolytics-dimension-repository_nwo" content="AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="906725444"><meta name="octolytics-dimension-repository_network_root_nwo" content="AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline"><meta name="turbo-body-classes" content="logged-out env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><meta name="msapplication-TileImage" content="/windows-tile.png"><meta name="msapplication-TileColor" content="#ffffff"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-out env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 15px;">
    <div data-turbo-body="" class="logged-out env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula#start-of-content" data-skip-target-assigned="false" class="px-2 py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/keyboard-shortcuts-dialog-958cae8ecd6c.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./createmain_files/primer-react.797c8ec006b327590422.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r5f:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




      

          

              
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-73b675cf164a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./createmain_files/sessions-5d6426bbf16a.js.download"></script>
<header class="HeaderMktg header-logged-out js-details-container js-header Details f4 py-3" role="banner" data-is-top="true" data-color-mode="light" data-light-theme="light" data-dark-theme="dark">
  <h2 class="sr-only">Navigation Menu</h2>

  <button type="button" class="HeaderMktg-backdrop d-lg-none border-0 position-fixed top-0 left-0 width-full height-full js-details-target" aria-label="Toggle navigation">
    <span class="d-none">Toggle navigation</span>
  </button>

  <div class="d-flex flex-column flex-lg-row flex-items-center px-3 px-md-4 px-lg-5 height-full position-relative z-1">
    <div class="d-flex flex-justify-between flex-items-center width-full width-lg-auto">
      <div class="flex-1">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target js-nav-padding-recalculate js-header-menu-toggle Button--link Button--medium Button d-lg-none color-fg-inherit p-1">  <span class="Button-content">
    <span class="Button-label"><div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div></span>
  </span>
</button>
      </div>

      <a class="mr-lg-3 color-fg-inherit flex-order-2 js-prevent-focus-on-mobile-nav" href="https://github.com/" aria-label="Homepage" data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Logomark;ref_loc:Header&quot;}">
        <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
      </a>

      <div class="flex-1 flex-order-2 text-right">
          <a href="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FAarthiVelpula%2FChat-with-PDF-Using-RAG-Pipeline%2Fcommits%3Fauthor%3DAarthiVelpula" class="HeaderMenu-link HeaderMenu-button d-inline-flex d-lg-none flex-order-1 f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="6c2961eb5b4e3176ec84273bb9ee28fdf46395e87384746032086d25d8a8af41" data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to Sign in&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}">
            Sign in
          </a>
      </div>
    </div>


    <div class="HeaderMenu js-header-menu height-fit position-lg-relative d-lg-flex flex-column flex-auto top-0">
      <div class="HeaderMenu-wrapper d-flex flex-column flex-self-start flex-lg-row flex-auto rounded rounded-lg-0">
          <nav class="HeaderMenu-nav" aria-label="Global">
            <ul class="d-lg-flex list-style-none">
                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Product
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 d-lg-flex flex-wrap dropdown-menu-wide">
          <div class="HeaderMenu-column px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_copilot&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_copilot_link_product_navbar&quot;}" href="https://github.com/features/copilot">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">GitHub Copilot</div>
        Write better code with AI
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;security&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;security_link_product_navbar&quot;}" href="https://github.com/features/security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Security</div>
        Find and fix vulnerabilities
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;actions&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;actions_link_product_navbar&quot;}" href="https://github.com/features/actions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-workflow color-fg-subtle mr-3">
    <path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Actions</div>
        Automate any workflow
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;codespaces&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;codespaces_link_product_navbar&quot;}" href="https://github.com/features/codespaces">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-codespaces color-fg-subtle mr-3">
    <path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Codespaces</div>
        Instant dev environments
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;issues&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;issues_link_product_navbar&quot;}" href="https://github.com/features/issues">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-issue-opened color-fg-subtle mr-3">
    <path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Issues</div>
        Plan and track work
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;code_review&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;code_review_link_product_navbar&quot;}" href="https://github.com/features/code-review">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-review color-fg-subtle mr-3">
    <path d="M10.3 6.74a.75.75 0 0 1-.04 1.06l-2.908 2.7 2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M1.5 4.25c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v12.5a1.75 1.75 0 0 1-1.75 1.75h-9.69l-3.573 3.573A1.458 1.458 0 0 1 5 21.043V18.5H3.25a1.75 1.75 0 0 1-1.75-1.75ZM3.25 4a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h2.5a.75.75 0 0 1 .75.75v3.19l3.72-3.72a.749.749 0 0 1 .53-.22h10a.25.25 0 0 0 .25-.25V4.25a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Code Review</div>
        Manage code changes
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;discussions&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;discussions_link_product_navbar&quot;}" href="https://github.com/features/discussions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Discussions</div>
        Collaborate outside of code
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;code_search&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;code_search_link_product_navbar&quot;}" href="https://github.com/features/code-search">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-square color-fg-subtle mr-3">
    <path d="M10.3 8.24a.75.75 0 0 1-.04 1.06L7.352 12l2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M2 3.75C2 2.784 2.784 2 3.75 2h16.5c.966 0 1.75.784 1.75 1.75v16.5A1.75 1.75 0 0 1 20.25 22H3.75A1.75 1.75 0 0 1 2 20.25Zm1.75-.25a.25.25 0 0 0-.25.25v16.5c0 .138.112.25.25.25h16.5a.25.25 0 0 0 .25-.25V3.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Code Search</div>
        Find more, search less
      </div>

    
</a></li>

                </ul>
              </div>
          </div>
          <div class="HeaderMenu-column px-lg-4">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="product-explore-heading">Explore</span>
                <ul class="list-style-none f5" aria-labelledby="product-explore-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;all_features&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;all_features_link_product_navbar&quot;}" href="https://github.com/features">
      All features

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;documentation&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;documentation_link_product_navbar&quot;}" href="https://docs.github.com/">
      Documentation

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_skills&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_skills_link_product_navbar&quot;}" href="https://skills.github.com/">
      GitHub Skills

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;blog&quot;,&quot;context&quot;:&quot;product&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;blog_link_product_navbar&quot;}" href="https://github.blog/">
      Blog

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>

                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Solutions
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 d-lg-flex flex-wrap dropdown-menu-wide">
          <div class="HeaderMenu-column px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0 pb-lg-3 mb-3 mb-lg-0">
                    <span class="d-block h4 color-fg-default my-1" id="solutions-by-company-size-heading">By company size</span>
                <ul class="list-style-none f5" aria-labelledby="solutions-by-company-size-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;enterprises&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;enterprises_link_solutions_navbar&quot;}" href="https://github.com/enterprise">
      Enterprises

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;small_and_medium_teams&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;small_and_medium_teams_link_solutions_navbar&quot;}" href="https://github.com/team">
      Small and medium teams

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;startups&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;startups_link_solutions_navbar&quot;}" href="https://github.com/enterprise/startups">
      Startups

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="solutions-by-use-case-heading">By use case</span>
                <ul class="list-style-none f5" aria-labelledby="solutions-by-use-case-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devsecops&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devsecops_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case/devsecops">
      DevSecOps

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devops&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devops_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case/devops">
      DevOps

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ci_cd&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ci_cd_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case/ci-cd">
      CI/CD

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_use_cases&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_use_cases_link_solutions_navbar&quot;}" href="https://github.com/solutions/use-case">
      View all use cases

    
</a></li>

                </ul>
              </div>
          </div>
          <div class="HeaderMenu-column px-lg-4">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="solutions-by-industry-heading">By industry</span>
                <ul class="list-style-none f5" aria-labelledby="solutions-by-industry-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;healthcare&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;healthcare_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/healthcare">
      Healthcare

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;financial_services&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;financial_services_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/financial-services">
      Financial services

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;manufacturing&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;manufacturing_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/manufacturing">
      Manufacturing

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;government&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;government_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry/government">
      Government

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all_industries&quot;,&quot;context&quot;:&quot;solutions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_industries_link_solutions_navbar&quot;}" href="https://github.com/solutions/industry">
      View all industries

    
</a></li>

                </ul>
              </div>
          </div>
         <div class="HeaderMenu-trailing-link rounded-bottom-2 flex-shrink-0 mt-lg-4 px-lg-4 py-4 py-lg-3 f5 text-semibold">
            <a href="https://github.com/solutions">
              View all solutions
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right HeaderMenu-trailing-link-icon">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</a>         </div>
      </div>
</li>

                  <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Resources
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 d-lg-flex flex-wrap dropdown-menu-wide">
          <div class="HeaderMenu-column px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="resources-topics-heading">Topics</span>
                <ul class="list-style-none f5" aria-labelledby="resources-topics-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;ai&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;ai_link_resources_navbar&quot;}" href="https://github.com/resources/articles/ai">
      AI

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;devops&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;devops_link_resources_navbar&quot;}" href="https://github.com/resources/articles/devops">
      DevOps

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;security&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;security_link_resources_navbar&quot;}" href="https://github.com/resources/articles/security">
      Security

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;software_development&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;software_development_link_resources_navbar&quot;}" href="https://github.com/resources/articles/software-development">
      Software Development

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;view_all&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;view_all_link_resources_navbar&quot;}" href="https://github.com/resources/articles">
      View all

    
</a></li>

                </ul>
              </div>
          </div>
          <div class="HeaderMenu-column px-lg-4">
              <div class="border-bottom pb-3 pb-lg-0 border-lg-bottom-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="resources-explore-heading">Explore</span>
                <ul class="list-style-none f5" aria-labelledby="resources-explore-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;learning_pathways&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;learning_pathways_link_resources_navbar&quot;}" href="https://resources.github.com/learn/pathways">
      Learning Pathways

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;white_papers_ebooks_webinars&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;white_papers_ebooks_webinars_link_resources_navbar&quot;}" href="https://resources.github.com/">
      White papers, Ebooks, Webinars

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;customer_stories&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;customer_stories_link_resources_navbar&quot;}" href="https://github.com/customer-stories">
      Customer Stories

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary Link--external" target="_blank" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;partners&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;partners_link_resources_navbar&quot;}" href="https://partner.github.com/">
      Partners

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;executive_insights&quot;,&quot;context&quot;:&quot;resources&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;executive_insights_link_resources_navbar&quot;}" href="https://github.com/solutions/executive-insights">
      Executive Insights

    
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Open Source
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 px-lg-4">
          <div class="HeaderMenu-column">
              <div class="border-bottom pb-3 pb-lg-0 pb-lg-3 mb-3 mb-lg-0 mb-lg-3">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_sponsors&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_sponsors_link_open_source_navbar&quot;}" href="https://github.com/sponsors">
      
      <div>
        <div class="color-fg-default h4">GitHub Sponsors</div>
        Fund open source developers
      </div>

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 pb-lg-3 mb-3 mb-lg-0 mb-lg-3">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;the_readme_project&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;the_readme_project_link_open_source_navbar&quot;}" href="https://github.com/readme">
      
      <div>
        <div class="color-fg-default h4">The ReadME Project</div>
        GitHub community articles
      </div>

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="open-source-repositories-heading">Repositories</span>
                <ul class="list-style-none f5" aria-labelledby="open-source-repositories-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;topics&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;topics_link_open_source_navbar&quot;}" href="https://github.com/topics">
      Topics

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;trending&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;trending_link_open_source_navbar&quot;}" href="https://github.com/trending">
      Trending

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;collections&quot;,&quot;context&quot;:&quot;open_source&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;collections_link_open_source_navbar&quot;}" href="https://github.com/collections">
      Collections

    
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Enterprise
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 pt-2 pt-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 pb-2 pb-lg-4 px-lg-4">
          <div class="HeaderMenu-column">
              <div class="border-bottom pb-3 pb-lg-0 pb-lg-3 mb-3 mb-lg-0 mb-lg-3">
                <ul class="list-style-none f5">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;enterprise_platform&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;enterprise_platform_link_enterprise_navbar&quot;}" href="https://github.com/enterprise">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-stack color-fg-subtle mr-3">
    <path d="M11.063 1.456a1.749 1.749 0 0 1 1.874 0l8.383 5.316a1.751 1.751 0 0 1 0 2.956l-8.383 5.316a1.749 1.749 0 0 1-1.874 0L2.68 9.728a1.751 1.751 0 0 1 0-2.956Zm1.071 1.267a.25.25 0 0 0-.268 0L3.483 8.039a.25.25 0 0 0 0 .422l8.383 5.316a.25.25 0 0 0 .268 0l8.383-5.316a.25.25 0 0 0 0-.422Z"></path><path d="M1.867 12.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path><path d="M1.867 16.324a.75.75 0 0 1 1.035-.232l8.964 5.685a.25.25 0 0 0 .268 0l8.964-5.685a.75.75 0 0 1 .804 1.267l-8.965 5.685a1.749 1.749 0 0 1-1.874 0l-8.965-5.685a.75.75 0 0 1-.231-1.035Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Enterprise platform</div>
        AI-powered developer platform
      </div>

    
</a></li>

                </ul>
              </div>
              <div class="border-bottom pb-3 pb-lg-0 border-bottom-0">
                    <span class="d-block h4 color-fg-default my-1" id="enterprise-available-add-ons-heading">Available add-ons</span>
                <ul class="list-style-none f5" aria-labelledby="enterprise-available-add-ons-heading">
                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;advanced_security&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;advanced_security_link_enterprise_navbar&quot;}" href="https://github.com/enterprise/advanced-security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Advanced Security</div>
        Enterprise-grade security features
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description pb-lg-3" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;github_copilot&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;github_copilot_link_enterprise_navbar&quot;}" href="https://github.com/features/copilot#enterprise">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">GitHub Copilot</div>
        Enterprise-grade AI features
      </div>

    
</a></li>

                    <li>
  <a class="HeaderMenu-dropdown-link d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center Link--has-description" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;premium_support&quot;,&quot;context&quot;:&quot;enterprise&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;premium_support_link_enterprise_navbar&quot;}" href="https://github.com/premium-support">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Premium Support</div>
        Enterprise-grade 24/7 support
      </div>

    
</a></li>

                </ul>
              </div>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
    <a class="HeaderMenu-link no-underline px-0 px-lg-2 py-3 py-lg-2 d-block d-lg-inline-block" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;pricing&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;pricing_link_global_navbar&quot;}" href="https://github.com/pricing">Pricing</a>
</li>

            </ul>
          </nav>

        <div class="d-flex flex-column flex-lg-row width-full flex-justify-end flex-lg-items-center text-center mt-3 mt-lg-0 text-lg-left ml-lg-3">
                


<qbsearch-input class="search-input" data-scope="repo:AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="lFpVa6OKJ1iVGFoh0GqDhtyD8o6vds-TFPBvIn4B_NMhVgxO_81t71vqnUrEwU-TNEuzNvBckh6nwO2LfVJd4A" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline" data-current-org="" data-current-owner="AarthiVelpula" data-logged-in="false" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-retain-scroll-position="true" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center mr-4 rounded" data-action="click:qbsearch-input#searchInputContainerClicked">
      <button type="button" class="header-search-button placeholder input-button form-control d-flex flex-1 flex-self-stretch flex-items-center no-wrap width-full py-0 pl-2 pr-0 text-left border-0 box-shadow-none" data-target="qbsearch-input.inputButton" aria-label="Search or jump to…" aria-haspopup="dialog" placeholder="Search or jump to..." data-hotkey="s,/" autocapitalize="off" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" data-action="click:qbsearch-input#handleExpand">
        <div class="mr-2 color-fg-muted">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <span class="flex-1" data-target="qbsearch-input.inputButtonText">Search or jump to...</span>
          <div class="d-flex" data-target="qbsearch-input.hotkeyIndicator">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>

          </div>
      </button>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-large Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-fixed width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-c6ed43a7-17a9-425d-93ec-cdf4d2d47e89" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-c6ed43a7-17a9-425d-93ec-cdf4d2d47e89" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="U7AMPCQkRE0eM72ElzyO0VGQqOMWcQB3sEtmf6IAAWRn+/CHQNS3WaKZElASjuCnFCwj8Im5LoBNSmgEaXnDkg==">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="w1tLpstixGtyQS7GBPL8vrNY5ck2PUKBaBmWg39Fr4j74jYp3ta01OcL7/bNm8tTQlDbHCregiZFNTRBbWgjyA==">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" data-csrf="true" value="NF9rS7lFz5IOJBk2mX9etfDRCC5PJl0xL7p/kXTmhp159xMyHQpYH5H5YTycfMjtFJ/mTjmFM1xxA2h0Rfe3Zg==">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>

            <div class="position-relative HeaderMenu-link-wrap d-lg-inline-block">
              <a href="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FAarthiVelpula%2FChat-with-PDF-Using-RAG-Pipeline%2Fcommits%3Fauthor%3DAarthiVelpula" class="HeaderMenu-link HeaderMenu-link--sign-in HeaderMenu-button flex-shrink-0 no-underline d-none d-lg-inline-flex border border-lg-0 rounded rounded-lg-0 px-2 py-1" style="margin-left: 12px;" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="6c2961eb5b4e3176ec84273bb9ee28fdf46395e87384746032086d25d8a8af41" data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}">
                Sign in
              </a>
            </div>

              <a href="https://github.com/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fcommits%2Fshow&amp;source=header-repo&amp;source_repo=AarthiVelpula%2FChat-with-PDF-Using-RAG-Pipeline" class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="6c2961eb5b4e3176ec84273bb9ee28fdf46395e87384746032086d25d8a8af41" data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/commits/show;ref_cta:Sign up;ref_loc:header logged out&quot;}">
                Sign up
              </a>
          <button type="button" class="sr-only js-header-menu-focus-trap d-block d-lg-none">Reseting focus</button>
        </div>
      </div>
    </div>
  </div>
</header>

      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula">Reload</a> to refresh your session.</span>

    <button id="icon-button-dafe188e-92b5-45a0-bc2b-d2714bb84431" aria-labelledby="tooltip-6b17e408-5715-4bc5-aea5-4eddb75483a9" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-6b17e408-5715-4bc5-aea5-4eddb75483a9" for="icon-button-dafe188e-92b5-45a0-bc2b-d2714bb84431" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






  
  <div id="repository-container-header" class="pt-3 hide-full-screen" style="background-color: var(--page-header-bgColor, var(--color-page-header-bg));" data-turbo-replace="">

      <div class="d-flex flex-nowrap flex-justify-end mb-3  px-3 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit">
            
  <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo color-fg-muted mr-2">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/AarthiVelpula/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/AarthiVelpula">
        AarthiVelpula
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline">Chat-with-PDF-Using-RAG-Pipeline</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace="" style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      

  <li>
            <a href="https://github.com/login?return_to=%2FAarthiVelpula%2FChat-with-PDF-Using-RAG-Pipeline" rel="nofollow" id="repository-details-watch-button" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="02d4356bb8933ae9cf945960675ec29ab941463542813dec0b3f5da0dafa9319" aria-label="You must be signed in to change notification settings" data-view-component="true" class="btn-sm btn" aria-describedby="tooltip-42215c52-20f5-404c-8206-7587284c1b55">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>    <tool-tip id="tooltip-42215c52-20f5-404c-8206-7587284c1b55" for="repository-details-watch-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You must be signed in to change notification settings</tool-tip>

  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="https://github.com/login?return_to=%2FAarthiVelpula%2FChat-with-PDF-Using-RAG-Pipeline" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:906725444,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="133bc545721ba7af6c7d45e5589b1d613411b2d3f71d2a4cef9bdd8e3a2ad0c7" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="0" data-view-component="true" class="Counter">0</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="https://github.com/login?return_to=%2FAarthiVelpula%2FChat-with-PDF-Using-RAG-Pipeline" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:906725444,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="63bd5e7002ecf68abec0d2432c4d60863d2a7d764d5df07fd48cf13d3ac37bdd" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-sw btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="0 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="0" data-view-component="true" class="Counter js-social-count">0</span>
</a></div>
  </li>

</ul>

        </div>
      </div>

        <div id="responsive-meta-container" data-turbo-replace="">
</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-button" popovertarget="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-overlay" aria-controls="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-list" aria-haspopup="true" aria-labelledby="tooltip-2c124a5f-c5d5-49f8-be3a-d60bf0d837e6" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-2c124a5f-c5d5-49f8-be3a-d60bf0d837e6" for="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-overlay" anchor="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-button" id="action-menu-51ff77a7-0946-4fa8-91b6-6dc74c99bfc7-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-f6aa7730-5739-4659-b438-7d9c11802925" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-7315da44-6bb5-4e7c-bc72-f3519cbae030" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-ef0db4c6-677d-4130-831d-b80d012e7ffd" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-aa21f8f8-8f4f-4fd6-a647-92640cfbc8b3" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-b8772454-1d85-47f0-a851-ec1f090205c8" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-a91f85b5-2b70-4634-b4c2-ebb2b12849c8" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-a4ac5af3-dc43-4c5c-9892-a7b0a9b07116" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>

  </div>

  



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
    



    
      
    








<react-app app-name="commits" initial-path="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" style="display: block; min-height: calc(100vh - 64px);" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"commitGroups":[{"title":"Dec 21, 2024","commits":[{"oid":"9eab8d43b2cb8fc5bd7b12d488185c14d35962dd","url":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/9eab8d43b2cb8fc5bd7b12d488185c14d35962dd","authoredDate":"2024-12-21T23:50:26.000+05:30","committedDate":"2024-12-21T23:50:26.000+05:30","shortMessage":"Create page.css","shortMessageMarkdown":null,"shortMessageMarkdownLink":"\u003ca data-pjax=\"true\" title=\"Create page.css\" class=\"color-fg-default\" href=\"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/9eab8d43b2cb8fc5bd7b12d488185c14d35962dd\"\u003eCreate page.css\u003c/a\u003e","bodyMessageHtml":"","authors":[{"login":"AarthiVelpula","displayName":"Aarthi Velpula","avatarUrl":"https://avatars.githubusercontent.com/u/149761483?v=4","path":"/AarthiVelpula","isGitHub":false}],"committerAttribution":false,"committer":{"login":"web-flow","displayName":"GitHub","avatarUrl":"https://avatars.githubusercontent.com/u/19864447?v=4","path":"/web-flow","isGitHub":true}},{"oid":"248b23f7a7f893ad3c54b71a09da5d3721fef080","url":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/248b23f7a7f893ad3c54b71a09da5d3721fef080","authoredDate":"2024-12-21T23:49:36.000+05:30","committedDate":"2024-12-21T23:49:36.000+05:30","shortMessage":"Create page.js","shortMessageMarkdown":null,"shortMessageMarkdownLink":"\u003ca data-pjax=\"true\" title=\"Create page.js\" class=\"color-fg-default\" href=\"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/248b23f7a7f893ad3c54b71a09da5d3721fef080\"\u003eCreate page.js\u003c/a\u003e","bodyMessageHtml":"","authors":[{"login":"AarthiVelpula","displayName":"Aarthi Velpula","avatarUrl":"https://avatars.githubusercontent.com/u/149761483?v=4","path":"/AarthiVelpula","isGitHub":false}],"committerAttribution":false,"committer":{"login":"web-flow","displayName":"GitHub","avatarUrl":"https://avatars.githubusercontent.com/u/19864447?v=4","path":"/web-flow","isGitHub":true}},{"oid":"c34453a849295d11d201b2817871a48e2b3ef8aa","url":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/c34453a849295d11d201b2817871a48e2b3ef8aa","authoredDate":"2024-12-21T23:48:37.000+05:30","committedDate":"2024-12-21T23:48:37.000+05:30","shortMessage":"Create page.html","shortMessageMarkdown":null,"shortMessageMarkdownLink":"\u003ca data-pjax=\"true\" title=\"Create page.html\" class=\"color-fg-default\" href=\"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/c34453a849295d11d201b2817871a48e2b3ef8aa\"\u003eCreate page.html\u003c/a\u003e","bodyMessageHtml":"","authors":[{"login":"AarthiVelpula","displayName":"Aarthi Velpula","avatarUrl":"https://avatars.githubusercontent.com/u/149761483?v=4","path":"/AarthiVelpula","isGitHub":false}],"committerAttribution":false,"committer":{"login":"web-flow","displayName":"GitHub","avatarUrl":"https://avatars.githubusercontent.com/u/19864447?v=4","path":"/web-flow","isGitHub":true}},{"oid":"88992030933f1f99ebfa69cefcf6d4d527d0b785","url":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/88992030933f1f99ebfa69cefcf6d4d527d0b785","authoredDate":"2024-12-21T23:47:02.000+05:30","committedDate":"2024-12-21T23:47:02.000+05:30","shortMessage":"Create main.py","shortMessageMarkdown":null,"shortMessageMarkdownLink":"\u003ca data-pjax=\"true\" title=\"Create main.py\" class=\"color-fg-default\" href=\"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/88992030933f1f99ebfa69cefcf6d4d527d0b785\"\u003eCreate main.py\u003c/a\u003e","bodyMessageHtml":"","authors":[{"login":"AarthiVelpula","displayName":"Aarthi Velpula","avatarUrl":"https://avatars.githubusercontent.com/u/149761483?v=4","path":"/AarthiVelpula","isGitHub":false}],"committerAttribution":false,"committer":{"login":"web-flow","displayName":"GitHub","avatarUrl":"https://avatars.githubusercontent.com/u/19864447?v=4","path":"/web-flow","isGitHub":true}},{"oid":"bd7650c35a95ded6cec87ad29986672a6a6dad88","url":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/bd7650c35a95ded6cec87ad29986672a6a6dad88","authoredDate":"2024-12-21T23:45:36.000+05:30","committedDate":"2024-12-21T23:45:36.000+05:30","shortMessage":"Update README.md","shortMessageMarkdown":null,"shortMessageMarkdownLink":"\u003ca data-pjax=\"true\" title=\"Update README.md\" class=\"color-fg-default\" href=\"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/bd7650c35a95ded6cec87ad29986672a6a6dad88\"\u003eUpdate README.md\u003c/a\u003e","bodyMessageHtml":"","authors":[{"login":"AarthiVelpula","displayName":"Aarthi Velpula","avatarUrl":"https://avatars.githubusercontent.com/u/149761483?v=4","path":"/AarthiVelpula","isGitHub":false}],"committerAttribution":false,"committer":{"login":"web-flow","displayName":"GitHub","avatarUrl":"https://avatars.githubusercontent.com/u/19864447?v=4","path":"/web-flow","isGitHub":true}},{"oid":"ac3f863701182b51b0fbda556a2a594ba7a66492","url":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/ac3f863701182b51b0fbda556a2a594ba7a66492","authoredDate":"2024-12-21T23:40:02.000+05:30","committedDate":"2024-12-21T23:40:02.000+05:30","shortMessage":"Initial commit","shortMessageMarkdown":null,"shortMessageMarkdownLink":"\u003ca data-pjax=\"true\" title=\"Initial commit\" class=\"color-fg-default\" href=\"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/ac3f863701182b51b0fbda556a2a594ba7a66492\"\u003eInitial commit\u003c/a\u003e","bodyMessageHtml":"","authors":[{"login":"AarthiVelpula","displayName":"Aarthi Velpula","avatarUrl":"https://avatars.githubusercontent.com/u/149761483?v=4","path":"/AarthiVelpula","isGitHub":false}],"committerAttribution":false,"committer":{"login":"web-flow","displayName":"GitHub","avatarUrl":"https://avatars.githubusercontent.com/u/19864447?v=4","path":"/web-flow","isGitHub":true}}]}],"currentCommit":{"oid":"9eab8d43b2cb8fc5bd7b12d488185c14d35962dd"},"filters":{"since":null,"until":null,"author":{"primaryAvatarUrl":"https://avatars.githubusercontent.com/u/149761483?v=4","path":"/AarthiVelpula","login":"AarthiVelpula","name":null},"newPath":null,"originalBranch":null,"currentBlobPath":null,"pagination":{"startCursor":"9eab8d43b2cb8fc5bd7b12d488185c14d35962dd 0","endCursor":"9eab8d43b2cb8fc5bd7b12d488185c14d35962dd 5","hasNextPage":false,"hasPreviousPage":false}},"metadata":{"browsingRenameHistory":null,"showProfileHelp":false,"deferredDataUrl":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits/deferred_commit_data/main?author=AarthiVelpula","deferredContributorUrl":"/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits/deferred_commit_contributors","softNavToCommit":false},"repo":{"id":906725444,"defaultBranch":"main","name":"Chat-with-PDF-Using-RAG-Pipeline","ownerLogin":"AarthiVelpula","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2024-12-21T18:10:02.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/149761483?v=4","public":true,"private":false,"isOrgOwned":false},"refInfo":{"name":"main","listCacheKey":"v0:1734804602.0","refType":"branch","currentOid":"9eab8d43b2cb8fc5bd7b12d488185c14d35962dd"},"timedOutMessage":""},"title":"Commits · AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline","appPayload":{"helpUrl":"https://docs.github.com","enabled_features":{"commits_ux_refresh_compare":false,"commit_details_extra_diff_fetching":false}}}</script>
  <div data-target="react-app.reactRoot"> <!-- --> <div style="--sticky-pane-height:100vh;--spacing:var(--spacing-normal)" class="Box-sc-g0xbh4-0 kkWQEA"><div class="Box-sc-g0xbh4-0 bSJDXx"><header class="Box-sc-g0xbh4-0 jPRcNF"><div class="Box-sc-g0xbh4-0 hOfjFo"><div class="d-flex flex-items-center flex-justify-between"><h1 class="f2 text-normal pb-2 prc-Heading-Heading-6CmGO" id="commits-pagehead">Commits</h1></div></div><div class="Box-sc-g0xbh4-0 gKBBxN"></div></header><div class="Box-sc-g0xbh4-0 kowOcT"><div class="Box-sc-g0xbh4-0 dQkwwl"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 FxAyp"><div><div class="Box-sc-g0xbh4-0 gwHaUx"><h2 class="sr-only prc-Heading-Heading-6CmGO">Branch selector</h2><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" data-hotkey="w" aria-label="main branch" data-testid="anchor-button" class="Box-sc-g0xbh4-0 dmxRgG prc-Button-ButtonBase-c50BI" data-loading="false" data-size="medium" data-variant="default" aria-describedby="branch-picker-commits-loading-announcement" id="branch-picker-commits"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="Box-sc-g0xbh4-0 bZBlpz"><div class="Box-sc-g0xbh4-0 lhTYNA"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 dbrgmi ref-selector-button-text-container"><span class="Text__StyledText-sc-17v1xeu-0 eMMFM">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey="w" data-hotkey-scope="read-only-cursor-text-area"></button><div class="d-flex flex-column flex-sm-row gap-2"><h2 class="sr-only prc-Heading-Heading-6CmGO">User selector</h2><div><button type="button" data-testid="user-selector-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI" data-loading="false" data-size="medium" data-variant="default" aria-describedby=":R1crab:-loading-announcement" id=":R1crab:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="Box-sc-g0xbh4-0 cSURfY"><div class="Box-sc-g0xbh4-0 hjDqIa"><img data-component="Avatar" class="prc-Avatar-Avatar-ZRS-m" alt="" width="16" height="16" style="--avatarSize-regular:16px" src="./createmain_files/149761483" data-testid="github-avatar"></div><div class="Box-sc-g0xbh4-0 dGVxWp"><span>AarthiVelpula</span></div></div></span></span><span data-component="trailingAction" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button></div><h2 class="sr-only prc-Heading-Heading-6CmGO">Datepicker</h2><button type="button" aria-haspopup="true" tabindex="0" data-testid="date-picker-commits" class="prc-Button-ButtonBase-c50BI" data-loading="false" data-size="medium" data-variant="default" aria-describedby=":r5h:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0 WGJwj fgColor-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M4.75 0a.75.75 0 0 1 .75.75V2h5V.75a.75.75 0 0 1 1.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 0 1 4.75 0ZM2.5 7.5v6.75c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V7.5Zm10.75-4H2.75a.25.25 0 0 0-.25.25V6h11V3.75a.25.25 0 0 0-.25-.25Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">All time</span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button></div></div><div class="mb-3" data-hpc="true"><h2 class="sr-only prc-Heading-Heading-6CmGO">Commit History</h2><div class="Timeline__ToggleTimeline-sc-1nkzbnu-0 eSFHqT"><div style="display:contents"><div class="Timeline__ToggleTimelineItem-sc-1nkzbnu-1 fhQhVG Timeline-Item"><div class="Box-sc-g0xbh4-0 izArLR"><div display="flex" class="Box-sc-g0xbh4-0 bbNsBg TimelineItem-Badge" overflow="hidden" color="fg.muted" width="32px" height="32px"><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M11.93 8.5a4.002 4.002 0 0 1-7.86 0H.75a.75.75 0 0 1 0-1.5h3.32a4.002 4.002 0 0 1 7.86 0h3.32a.75.75 0 0 1 0 1.5Zm-1.43-.75a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg></div></div><div class="Timeline__ToggleTimelineBody-sc-1nkzbnu-2 jdZjlQ mt-0"><h3 class="text-normal f5 py-1 prc-Heading-Heading-6CmGO" id=":Rt5rab:" data-testid="commit-group-title">Commits on Dec 21, 2024</h3><div class="color-bg-default position-relative border rounded-2 color-border-default mt-2 d-flex flex-column CommitGroup-module__panel--tvFMx"><div id=":Rlt5rab:-list-view-container" class="ListView-module__container--zF6wW"><ul class="Box-sc-g0xbh4-0 ListView-module__ul--vMLEZ" aria-labelledby=":Rt5rab:" tabindex="-1" role="list" data-listview-component="items-list" data-testid="list-view-items"><li id=":Rlt5rab:-list-view-node-:R2flt5rab:" role="listitem" class="Box-sc-g0xbh4-0 cdHayA ListItem-module__listItem--kHali" tabindex="-1" aria-label="Create page.css. More information available below." data-testid="commit-row-item" data-commit-link="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/9eab8d43b2cb8fc5bd7b12d488185c14d35962dd"><div data-testid="list-view-item-title-container" class="Box-sc-g0xbh4-0 jJRiHe Title-module__container--l9xi7"><h4 class="Text__StyledText-sc-17v1xeu-0 ljLSiW markdown-title Title-module__heading--upUxW"><span class="Text__StyledText-sc-17v1xeu-0 hWqAbU TitleHeader-module__inline--rL27T Title-module__anchor--SyQM6 Title-module__markdown--KiFgL"><a data-pjax="true" title="Create page.css" class="color-fg-default" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/9eab8d43b2cb8fc5bd7b12d488185c14d35962dd" tabindex="-1">Create page.css</a></span></h4><span class="Title-module__trailingBadgesContainer--XGsbF"></span></div><div class="px-1"></div><div data-testid="list-view-item-main-content" class="MainContent-module__container--ry4iL"><div class="MainContent-module__inner--bU_tk"><div data-testid="list-view-item-description" class="Box-sc-g0xbh4-0 Description-module__container--b3n6F"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/AarthiVelpula" data-testid="avatar-icon-link" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1"><img data-component="Avatar" class="Box-sc-g0xbh4-0 bbHsCC prc-Avatar-Avatar-ZRS-m" alt="AarthiVelpula" width="16" height="16" style="--avatarSize-regular:16px" src="./createmain_files/149761483" data-testid="github-avatar" aria-label="AarthiVelpula"></a><a class="Box-sc-g0xbh4-0 jRhDJg prc-Link-Link-85e08" data-muted="true" muted="" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" aria-label="commits by AarthiVelpula" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1">AarthiVelpula</a></div><span class="pl-1">authored</span><relative-time class="sc-aXZVg pl-1" datetime="2024-12-21T18:20:26.000Z" title="Dec 21, 2024, 11:50 PM GMT+5:30"><template shadowrootmode="open">25 minutes ago</template>Dec 21, 2024</relative-time><div class="d-none d-sm-flex"></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MetadataContainer-module__container--lj6YE" data-testid="list-view-item-metadata"><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 EDqVA Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"><button class="Box-sc-g0xbh4-0 bqPywI prc-Label-Label--LG6X" data-size="small" data-variant="success" tabindex="-1">Verified</button></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__primary--cJgJU d-none d-sm-flex px-0 gap-2"><div class="d-flex"><span role="tooltip" aria-label="View commit details" id=":R2tqflt5rab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-s"><a class="Button--invisible Button--small Button text-mono" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/9eab8d43b2cb8fc5bd7b12d488185c14d35962dd" variant="invisible" sx="[object Object]" tabindex="-1"><span class="Button-content"><span class="Button-label color-fg-muted">9eab8d4</span></span></a></span><div><div aria-describedby=":R4tqflt5rab:"><button aria-label="Copy full SHA for 9eab8d4" tabindex="-1" class="Button Button--iconOnly Button--invisible Button--small "><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div><span role="tooltip" aria-label="Browse repository at this point" id="browse-repo-9eab8d4" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-sw"><a aria-labelledby="browse-repo-9eab8d4" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/tree/9eab8d43b2cb8fc5bd7b12d488185c14d35962dd" class="Button Button--iconOnly Button--invisible Button--small" data-testid="commit-row-browse-repo" tabindex="-1"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></a></span></div></div><div class="Box-sc-g0xbh4-0 izFOf ActionBar-module__container--ZVTfi" data-testid="list-view-item-action-bar-container"><div data-testid="action-bar-container" class="VisibleAndOverflowContainer-module__Box_0--cTFgm" style="gap: var(--base-size-8);"><div data-testid="action-bar" class="VisibleItems-module__Box_1--_dgKR" style="gap: var(--base-size-8);"></div><button data-component="IconButton" type="button" data-testid="overflow-menu-anchor" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI OverflowMenu-module__IconButton_0--P3118 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r5j:-loading-announcement" aria-labelledby=":r5l:" id=":r5j:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="Tooltip__StyledTooltip-sc-e45c7z-0 jOyaRH" data-direction="s" aria-hidden="true" id=":r5l:" popover="auto">More actions</span></div></div></li><li id=":Rlt5rab:-list-view-node-:R2nlt5rab:" role="listitem" class="Box-sc-g0xbh4-0 cdHayA ListItem-module__listItem--kHali" tabindex="-1" aria-label="Create page.js. More information available below." data-testid="commit-row-item" data-commit-link="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/248b23f7a7f893ad3c54b71a09da5d3721fef080"><div data-testid="list-view-item-title-container" class="Box-sc-g0xbh4-0 jJRiHe Title-module__container--l9xi7"><h4 class="Text__StyledText-sc-17v1xeu-0 ljLSiW markdown-title Title-module__heading--upUxW"><span class="Text__StyledText-sc-17v1xeu-0 hWqAbU TitleHeader-module__inline--rL27T Title-module__anchor--SyQM6 Title-module__markdown--KiFgL"><a data-pjax="true" title="Create page.js" class="color-fg-default" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/248b23f7a7f893ad3c54b71a09da5d3721fef080" tabindex="-1">Create page.js</a></span></h4><span class="Title-module__trailingBadgesContainer--XGsbF"></span></div><div class="px-1"></div><div data-testid="list-view-item-main-content" class="MainContent-module__container--ry4iL"><div class="MainContent-module__inner--bU_tk"><div data-testid="list-view-item-description" class="Box-sc-g0xbh4-0 Description-module__container--b3n6F"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/AarthiVelpula" data-testid="avatar-icon-link" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1"><img data-component="Avatar" class="Box-sc-g0xbh4-0 bbHsCC prc-Avatar-Avatar-ZRS-m" alt="AarthiVelpula" width="16" height="16" style="--avatarSize-regular:16px" src="./createmain_files/149761483" data-testid="github-avatar" aria-label="AarthiVelpula"></a><a class="Box-sc-g0xbh4-0 jRhDJg prc-Link-Link-85e08" data-muted="true" muted="" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" aria-label="commits by AarthiVelpula" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1">AarthiVelpula</a></div><span class="pl-1">authored</span><relative-time class="sc-aXZVg pl-1" datetime="2024-12-21T18:19:36.000Z" title="Dec 21, 2024, 11:49 PM GMT+5:30"><template shadowrootmode="open">25 minutes ago</template>Dec 21, 2024</relative-time><div class="d-none d-sm-flex"></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MetadataContainer-module__container--lj6YE" data-testid="list-view-item-metadata"><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 EDqVA Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"><button class="Box-sc-g0xbh4-0 bqPywI prc-Label-Label--LG6X" data-size="small" data-variant="success" tabindex="-1">Verified</button></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__primary--cJgJU d-none d-sm-flex px-0 gap-2"><div class="d-flex"><span role="tooltip" aria-label="View commit details" id=":R2tqnlt5rab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-s"><a class="Button--invisible Button--small Button text-mono" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/248b23f7a7f893ad3c54b71a09da5d3721fef080" variant="invisible" sx="[object Object]" tabindex="-1"><span class="Button-content"><span class="Button-label color-fg-muted">248b23f</span></span></a></span><div><div aria-describedby=":R4tqnlt5rab:"><button aria-label="Copy full SHA for 248b23f" tabindex="-1" class="Button Button--iconOnly Button--invisible Button--small "><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div><span role="tooltip" aria-label="Browse repository at this point" id="browse-repo-248b23f" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-sw"><a aria-labelledby="browse-repo-248b23f" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/tree/248b23f7a7f893ad3c54b71a09da5d3721fef080" class="Button Button--iconOnly Button--invisible Button--small" data-testid="commit-row-browse-repo" tabindex="-1"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></a></span></div></div><div class="Box-sc-g0xbh4-0 izFOf ActionBar-module__container--ZVTfi" data-testid="list-view-item-action-bar-container"><div data-testid="action-bar-container" class="VisibleAndOverflowContainer-module__Box_0--cTFgm" style="gap: var(--base-size-8);"><div data-testid="action-bar" class="VisibleItems-module__Box_1--_dgKR" style="gap: var(--base-size-8);"></div><button data-component="IconButton" type="button" data-testid="overflow-menu-anchor" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI OverflowMenu-module__IconButton_0--P3118 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r5n:-loading-announcement" aria-labelledby=":r5p:" id=":r5n:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="Tooltip__StyledTooltip-sc-e45c7z-0 jOyaRH" data-direction="s" aria-hidden="true" id=":r5p:" popover="auto">More actions</span></div></div></li><li id=":Rlt5rab:-list-view-node-:R2vlt5rab:" role="listitem" class="Box-sc-g0xbh4-0 cdHayA ListItem-module__listItem--kHali" tabindex="0" aria-label="Create page.html. More information available below." data-testid="commit-row-item" data-commit-link="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/c34453a849295d11d201b2817871a48e2b3ef8aa"><div data-testid="list-view-item-title-container" class="Box-sc-g0xbh4-0 jJRiHe Title-module__container--l9xi7"><h4 class="Text__StyledText-sc-17v1xeu-0 ljLSiW markdown-title Title-module__heading--upUxW"><span class="Text__StyledText-sc-17v1xeu-0 hWqAbU TitleHeader-module__inline--rL27T Title-module__anchor--SyQM6 Title-module__markdown--KiFgL"><a data-pjax="true" title="Create page.html" class="color-fg-default" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/c34453a849295d11d201b2817871a48e2b3ef8aa" tabindex="-1">Create page.html</a></span></h4><span class="Title-module__trailingBadgesContainer--XGsbF"></span></div><div class="px-1"></div><div data-testid="list-view-item-main-content" class="MainContent-module__container--ry4iL"><div class="MainContent-module__inner--bU_tk"><div data-testid="list-view-item-description" class="Box-sc-g0xbh4-0 Description-module__container--b3n6F"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/AarthiVelpula" data-testid="avatar-icon-link" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1"><img data-component="Avatar" class="Box-sc-g0xbh4-0 bbHsCC prc-Avatar-Avatar-ZRS-m" alt="AarthiVelpula" width="16" height="16" style="--avatarSize-regular:16px" src="./createmain_files/149761483" data-testid="github-avatar" aria-label="AarthiVelpula"></a><a class="Box-sc-g0xbh4-0 jRhDJg prc-Link-Link-85e08" data-muted="true" muted="" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" aria-label="commits by AarthiVelpula" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1">AarthiVelpula</a></div><span class="pl-1">authored</span><relative-time class="sc-aXZVg pl-1" datetime="2024-12-21T18:18:37.000Z" title="Dec 21, 2024, 11:48 PM GMT+5:30"><template shadowrootmode="open">26 minutes ago</template>Dec 21, 2024</relative-time><div class="d-none d-sm-flex"></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MetadataContainer-module__container--lj6YE" data-testid="list-view-item-metadata"><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 EDqVA Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"><button class="Box-sc-g0xbh4-0 bqPywI prc-Label-Label--LG6X" data-size="small" data-variant="success" tabindex="-1">Verified</button></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__primary--cJgJU d-none d-sm-flex px-0 gap-2"><div class="d-flex"><span role="tooltip" aria-label="View commit details" id=":R2tqvlt5rab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-s"><a class="Button--invisible Button--small Button text-mono" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/c34453a849295d11d201b2817871a48e2b3ef8aa" variant="invisible" sx="[object Object]" tabindex="-1"><span class="Button-content"><span class="Button-label color-fg-muted">c34453a</span></span></a></span><div><div aria-describedby=":R4tqvlt5rab:"><button aria-label="Copy full SHA for c34453a" tabindex="-1" class="Button Button--iconOnly Button--invisible Button--small "><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div><span role="tooltip" aria-label="Browse repository at this point" id="browse-repo-c34453a" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-sw"><a aria-labelledby="browse-repo-c34453a" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/tree/c34453a849295d11d201b2817871a48e2b3ef8aa" class="Button Button--iconOnly Button--invisible Button--small" data-testid="commit-row-browse-repo" tabindex="-1"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></a></span></div></div><div class="Box-sc-g0xbh4-0 izFOf ActionBar-module__container--ZVTfi" data-testid="list-view-item-action-bar-container"><div data-testid="action-bar-container" class="VisibleAndOverflowContainer-module__Box_0--cTFgm" style="gap: var(--base-size-8);"><div data-testid="action-bar" class="VisibleItems-module__Box_1--_dgKR" style="gap: var(--base-size-8);"></div><button data-component="IconButton" type="button" data-testid="overflow-menu-anchor" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI OverflowMenu-module__IconButton_0--P3118 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r5r:-loading-announcement" aria-labelledby=":r5t:" id=":r5r:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="Tooltip__StyledTooltip-sc-e45c7z-0 jOyaRH" data-direction="s" aria-hidden="true" id=":r5t:" popover="auto">More actions</span></div></div></li><li id=":Rlt5rab:-list-view-node-:R37lt5rab:" role="listitem" class="Box-sc-g0xbh4-0 cdHayA ListItem-module__listItem--kHali" tabindex="-1" aria-label="Create main.py. More information available below." data-testid="commit-row-item" data-commit-link="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/88992030933f1f99ebfa69cefcf6d4d527d0b785"><div data-testid="list-view-item-title-container" class="Box-sc-g0xbh4-0 jJRiHe Title-module__container--l9xi7"><h4 class="Text__StyledText-sc-17v1xeu-0 ljLSiW markdown-title Title-module__heading--upUxW"><span class="Text__StyledText-sc-17v1xeu-0 hWqAbU TitleHeader-module__inline--rL27T Title-module__anchor--SyQM6 Title-module__markdown--KiFgL"><a data-pjax="true" title="Create main.py" class="color-fg-default" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/88992030933f1f99ebfa69cefcf6d4d527d0b785" tabindex="-1">Create main.py</a></span></h4><span class="Title-module__trailingBadgesContainer--XGsbF"></span></div><div class="px-1"></div><div data-testid="list-view-item-main-content" class="MainContent-module__container--ry4iL"><div class="MainContent-module__inner--bU_tk"><div data-testid="list-view-item-description" class="Box-sc-g0xbh4-0 Description-module__container--b3n6F"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/AarthiVelpula" data-testid="avatar-icon-link" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1"><img data-component="Avatar" class="Box-sc-g0xbh4-0 bbHsCC prc-Avatar-Avatar-ZRS-m" alt="AarthiVelpula" width="16" height="16" style="--avatarSize-regular:16px" src="./createmain_files/149761483" data-testid="github-avatar" aria-label="AarthiVelpula"></a><a class="Box-sc-g0xbh4-0 jRhDJg prc-Link-Link-85e08" data-muted="true" muted="" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" aria-label="commits by AarthiVelpula" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1">AarthiVelpula</a></div><span class="pl-1">authored</span><relative-time class="sc-aXZVg pl-1" datetime="2024-12-21T18:17:02.000Z" title="Dec 21, 2024, 11:47 PM GMT+5:30"><template shadowrootmode="open">28 minutes ago</template>Dec 21, 2024</relative-time><div class="d-none d-sm-flex"></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MetadataContainer-module__container--lj6YE" data-testid="list-view-item-metadata"><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 EDqVA Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"><button class="Box-sc-g0xbh4-0 bqPywI prc-Label-Label--LG6X" data-size="small" data-variant="success" tabindex="-1">Verified</button></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__primary--cJgJU d-none d-sm-flex px-0 gap-2"><div class="d-flex"><span role="tooltip" aria-label="View commit details" id=":R2tr7lt5rab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-s"><a class="Button--invisible Button--small Button text-mono" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/88992030933f1f99ebfa69cefcf6d4d527d0b785" variant="invisible" sx="[object Object]" tabindex="-1"><span class="Button-content"><span class="Button-label color-fg-muted">8899203</span></span></a></span><div><div aria-describedby=":R4tr7lt5rab:"><button aria-label="Copy full SHA for 8899203" tabindex="-1" class="Button Button--iconOnly Button--invisible Button--small "><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div><span role="tooltip" aria-label="Browse repository at this point" id="browse-repo-8899203" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-sw"><a aria-labelledby="browse-repo-8899203" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/tree/88992030933f1f99ebfa69cefcf6d4d527d0b785" class="Button Button--iconOnly Button--invisible Button--small" data-testid="commit-row-browse-repo" tabindex="-1"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></a></span></div></div><div class="Box-sc-g0xbh4-0 izFOf ActionBar-module__container--ZVTfi" data-testid="list-view-item-action-bar-container"><div data-testid="action-bar-container" class="VisibleAndOverflowContainer-module__Box_0--cTFgm" style="gap: var(--base-size-8);"><div data-testid="action-bar" class="VisibleItems-module__Box_1--_dgKR" style="gap: var(--base-size-8);"></div><button data-component="IconButton" type="button" data-testid="overflow-menu-anchor" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI OverflowMenu-module__IconButton_0--P3118 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r5v:-loading-announcement" aria-labelledby=":r61:" id=":r5v:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="Tooltip__StyledTooltip-sc-e45c7z-0 jOyaRH" data-direction="s" aria-hidden="true" id=":r61:" popover="auto">More actions</span></div></div></li><li id=":Rlt5rab:-list-view-node-:R3flt5rab:" role="listitem" class="Box-sc-g0xbh4-0 cdHayA ListItem-module__listItem--kHali" tabindex="-1" aria-label="Update README.md. More information available below." data-testid="commit-row-item" data-commit-link="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/bd7650c35a95ded6cec87ad29986672a6a6dad88"><div data-testid="list-view-item-title-container" class="Box-sc-g0xbh4-0 jJRiHe Title-module__container--l9xi7"><h4 class="Text__StyledText-sc-17v1xeu-0 ljLSiW markdown-title Title-module__heading--upUxW"><span class="Text__StyledText-sc-17v1xeu-0 hWqAbU TitleHeader-module__inline--rL27T Title-module__anchor--SyQM6 Title-module__markdown--KiFgL"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/bd7650c35a95ded6cec87ad29986672a6a6dad88" tabindex="-1">Update README.md</a></span></h4><span class="Title-module__trailingBadgesContainer--XGsbF"></span></div><div class="px-1"></div><div data-testid="list-view-item-main-content" class="MainContent-module__container--ry4iL"><div class="MainContent-module__inner--bU_tk"><div data-testid="list-view-item-description" class="Box-sc-g0xbh4-0 Description-module__container--b3n6F"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/AarthiVelpula" data-testid="avatar-icon-link" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1"><img data-component="Avatar" class="Box-sc-g0xbh4-0 bbHsCC prc-Avatar-Avatar-ZRS-m" alt="AarthiVelpula" width="16" height="16" style="--avatarSize-regular:16px" src="./createmain_files/149761483" data-testid="github-avatar" aria-label="AarthiVelpula"></a><a class="Box-sc-g0xbh4-0 jRhDJg prc-Link-Link-85e08" data-muted="true" muted="" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" aria-label="commits by AarthiVelpula" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1">AarthiVelpula</a></div><span class="pl-1">authored</span><relative-time class="sc-aXZVg pl-1" datetime="2024-12-21T18:15:36.000Z" title="Dec 21, 2024, 11:45 PM GMT+5:30"><template shadowrootmode="open">29 minutes ago</template>Dec 21, 2024</relative-time><div class="d-none d-sm-flex"></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MetadataContainer-module__container--lj6YE" data-testid="list-view-item-metadata"><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 EDqVA Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"><button class="Box-sc-g0xbh4-0 bqPywI prc-Label-Label--LG6X" data-size="small" data-variant="success" tabindex="-1">Verified</button></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__primary--cJgJU d-none d-sm-flex px-0 gap-2"><div class="d-flex"><span role="tooltip" aria-label="View commit details" id=":R2trflt5rab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-s"><a class="Button--invisible Button--small Button text-mono" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/bd7650c35a95ded6cec87ad29986672a6a6dad88" variant="invisible" sx="[object Object]" tabindex="-1"><span class="Button-content"><span class="Button-label color-fg-muted">bd7650c</span></span></a></span><div><div aria-describedby=":R4trflt5rab:"><button aria-label="Copy full SHA for bd7650c" tabindex="-1" class="Button Button--iconOnly Button--invisible Button--small "><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div><span role="tooltip" aria-label="Browse repository at this point" id="browse-repo-bd7650c" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-sw"><a aria-labelledby="browse-repo-bd7650c" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/tree/bd7650c35a95ded6cec87ad29986672a6a6dad88" class="Button Button--iconOnly Button--invisible Button--small" data-testid="commit-row-browse-repo" tabindex="-1"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></a></span></div></div><div class="Box-sc-g0xbh4-0 izFOf ActionBar-module__container--ZVTfi" data-testid="list-view-item-action-bar-container"><div data-testid="action-bar-container" class="VisibleAndOverflowContainer-module__Box_0--cTFgm" style="gap: var(--base-size-8);"><div data-testid="action-bar" class="VisibleItems-module__Box_1--_dgKR" style="gap: var(--base-size-8);"></div><button data-component="IconButton" type="button" data-testid="overflow-menu-anchor" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI OverflowMenu-module__IconButton_0--P3118 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r63:-loading-announcement" aria-labelledby=":r65:" id=":r63:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="Tooltip__StyledTooltip-sc-e45c7z-0 jOyaRH" data-direction="s" aria-hidden="true" id=":r65:" popover="auto">More actions</span></div></div></li><li id=":Rlt5rab:-list-view-node-:R3nlt5rab:" role="listitem" class="Box-sc-g0xbh4-0 cdHayA ListItem-module__listItem--kHali" tabindex="-1" aria-label="Initial commit. More information available below." data-testid="commit-row-item" data-commit-link="/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/ac3f863701182b51b0fbda556a2a594ba7a66492"><div data-testid="list-view-item-title-container" class="Box-sc-g0xbh4-0 jJRiHe Title-module__container--l9xi7"><h4 class="Text__StyledText-sc-17v1xeu-0 ljLSiW markdown-title Title-module__heading--upUxW"><span class="Text__StyledText-sc-17v1xeu-0 hWqAbU TitleHeader-module__inline--rL27T Title-module__anchor--SyQM6 Title-module__markdown--KiFgL"><a data-pjax="true" title="Initial commit" class="color-fg-default" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/ac3f863701182b51b0fbda556a2a594ba7a66492" tabindex="-1">Initial commit</a></span></h4><span class="Title-module__trailingBadgesContainer--XGsbF"></span></div><div class="px-1"></div><div data-testid="list-view-item-main-content" class="MainContent-module__container--ry4iL"><div class="MainContent-module__inner--bU_tk"><div data-testid="list-view-item-description" class="Box-sc-g0xbh4-0 Description-module__container--b3n6F"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/AarthiVelpula" data-testid="avatar-icon-link" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1"><img data-component="Avatar" class="Box-sc-g0xbh4-0 bbHsCC prc-Avatar-Avatar-ZRS-m" alt="AarthiVelpula" width="16" height="16" style="--avatarSize-regular:16px" src="./createmain_files/149761483" data-testid="github-avatar" aria-label="AarthiVelpula"></a><a class="Box-sc-g0xbh4-0 jRhDJg prc-Link-Link-85e08" data-muted="true" muted="" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commits?author=AarthiVelpula" aria-label="commits by AarthiVelpula" data-hovercard-url="/users/AarthiVelpula/hovercard" tabindex="-1">AarthiVelpula</a></div><span class="pl-1">authored</span><relative-time class="sc-aXZVg pl-1" datetime="2024-12-21T18:10:02.000Z" title="Dec 21, 2024, 11:40 PM GMT+5:30"><template shadowrootmode="open">35 minutes ago</template>Dec 21, 2024</relative-time><div class="d-none d-sm-flex"></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MetadataContainer-module__container--lj6YE" data-testid="list-view-item-metadata"><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 EDqVA Metadata-module__metadata--yvrod Metadata-module__secondary--zMgLx"><button class="Box-sc-g0xbh4-0 bqPywI prc-Label-Label--LG6X" data-size="small" data-variant="success" tabindex="-1">Verified</button></div><div data-testid="list-view-item-metadata-item" class="Box-sc-g0xbh4-0 Metadata-module__metadata--yvrod Metadata-module__primary--cJgJU d-none d-sm-flex px-0 gap-2"><div class="d-flex"><span role="tooltip" aria-label="View commit details" id=":R2trnlt5rab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-s"><a class="Button--invisible Button--small Button text-mono" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/commit/ac3f863701182b51b0fbda556a2a594ba7a66492" variant="invisible" sx="[object Object]" tabindex="-1"><span class="Button-content"><span class="Button-label color-fg-muted">ac3f863</span></span></a></span><div><div aria-describedby=":R4trnlt5rab:"><button aria-label="Copy full SHA for ac3f863" tabindex="-1" class="Button Button--iconOnly Button--invisible Button--small "><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div><span role="tooltip" aria-label="Browse repository at this point" id="browse-repo-ac3f863" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-sw"><a aria-labelledby="browse-repo-ac3f863" href="https://github.com/AarthiVelpula/Chat-with-PDF-Using-RAG-Pipeline/tree/ac3f863701182b51b0fbda556a2a594ba7a66492" class="Button Button--iconOnly Button--invisible Button--small" data-testid="commit-row-browse-repo" tabindex="-1"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></a></span></div></div><div class="Box-sc-g0xbh4-0 izFOf ActionBar-module__container--ZVTfi" data-testid="list-view-item-action-bar-container"><div data-testid="action-bar-container" class="VisibleAndOverflowContainer-module__Box_0--cTFgm" style="gap: var(--base-size-8);"><div data-testid="action-bar" class="VisibleItems-module__Box_1--_dgKR" style="gap: var(--base-size-8);"></div><button data-component="IconButton" type="button" data-testid="overflow-menu-anchor" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI OverflowMenu-module__IconButton_0--P3118 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r67:-loading-announcement" aria-labelledby=":r69:" id=":r67:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="Tooltip__StyledTooltip-sc-e45c7z-0 jOyaRH" data-direction="s" aria-hidden="true" id=":r69:" popover="auto">More actions</span></div></div></li></ul></div></div></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0"></div></div></div></div></div> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"day"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
</a>
      <span>
        © 2024 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>




    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>




    </div>

    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">Copied!</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div id="__primerPortalRoot__" style="position: absolute; top: 0px; left: 0px;"><div style="position: relative; z-index: 1;"><span role="tooltip" aria-label="Copy full SHA for 9eab8d4" data-visible-text="Copy full SHA for 9eab8d4" aria-hidden="true" id=":R4tqflt5rab:" class="ControlledTooltip__TooltipBase-sc-b39269ff-0 bWQkSs tooltipped-s" style="position: absolute; left: 657.2px; top: 378.45px;"></span></div><div style="position: relative; z-index: 1;"><span role="tooltip" aria-label="Copy full SHA for 248b23f" data-visible-text="Copy full SHA for 248b23f" aria-hidden="true" id=":R4tqnlt5rab:" class="ControlledTooltip__TooltipBase-sc-b39269ff-0 bWQkSs tooltipped-s" style="position: absolute; left: 657.2px; top: 443.35px;"></span></div><div style="position: relative; z-index: 1;"><span role="tooltip" aria-label="Copy full SHA for c34453a" data-visible-text="Copy full SHA for c34453a" aria-hidden="true" id=":R4tqvlt5rab:" class="ControlledTooltip__TooltipBase-sc-b39269ff-0 bWQkSs tooltipped-s" style="position: absolute; left: 657.2px; top: 508.25px;"></span></div><div style="position: relative; z-index: 1;"><span role="tooltip" aria-label="Copy full SHA for 8899203" data-visible-text="Copy full SHA for 8899203" aria-hidden="true" id=":R4tr7lt5rab:" class="ControlledTooltip__TooltipBase-sc-b39269ff-0 bWQkSs tooltipped-s" style="position: absolute; left: 657.2px; top: 573.15px;"></span></div><div style="position: relative; z-index: 1;"><span role="tooltip" aria-label="Copy full SHA for bd7650c" data-visible-text="Copy full SHA for bd7650c" aria-hidden="true" id=":R4trflt5rab:" class="ControlledTooltip__TooltipBase-sc-b39269ff-0 bWQkSs tooltipped-s" style="position: absolute; left: 657.2px; top: 638.05px;"></span></div><div style="position: relative; z-index: 1;"><span role="tooltip" aria-label="Copy full SHA for ac3f863" data-visible-text="Copy full SHA for ac3f863" aria-hidden="true" id=":R4trnlt5rab:" class="ControlledTooltip__TooltipBase-sc-b39269ff-0 bWQkSs tooltipped-s" style="position: absolute; left: 657.2px; top: 702.95px;"></span></div></div><div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive"></div></body></html>