# I want to call http://localhost:8888/generate with a JSON body, and save the result as a PPTX file.
import requests



def generate():
    url = "http://localhost:8888/generate"
    json_data = {
        "template": "/code/app/templates/template2.pptx",
        "slides": [
            {
                "title": "Dynamic Slide Title"
            },
            {
                "title": "Agenda",
                "content": ["* Introduction\n* Main Topic\n* Conclusion"]
            },
            {
                "title": "Intro - Test Client",
                "pictures": [
                    "https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/media/managed-virtual-network/diagram-managed-network.png?view=foundry-classic"
                ]
            },
            {
                "title": "Some Topic"
            },
            {

                "title": "We can now generate slides!",
                "content": ["We take a template PPTX with placeholders and fill them with data using Jinja2 templating."],
                "pictures": [
                   "https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Content-Card-Xbox-Controllers-Black-Detail"
                ]
            },
            {
                "title": "Comparison to Version 2",
                "text": ["version1", "version2"],
                "content": [
                    "Jinja2 templating\nstatic page count",
                    "Dynamic slide count\nmore flexible"
                ]
            },
            {
                "title": "Conclusion",
                "content": ["This is the conclusion slide."],
                "tables": [
                    { 
                        "headers": ["Year", "Earnings", "Profit"],
                        "rows": [
                            ["2023", 10000000, 2000000],
                            ["2024", 25000000, 4000000],
                            ["2025", 35000000, 6000000]
                        ]
                    }
                ]
            },
            {
                "title": "Thank you for your attention!",
                "subtitles": [
                    "Test Bot\n- test@nothing.com\n- 555-123-4567"
                ]
            }
        ]
    }

#     json_data = {
#         "template": "/code/app/templates/blank.pptx", 
#         "slides": [
#         {
#             "title": "Financial Research Agent",
#             "text": [
#                 "Ashish Talati\nPrincipal Solution Engineer at Microsoft"
#             ]
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 600292,
#                     "y": 1518228,
#                     "width": 11018524,
#                     "height": 448305
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 1,
#                     "text": "a",
#                     "x": 600292,
#                     "y": 1966530,
#                     "width": 11018524,
#                     "height": 4782668
#                 },
#                 {
#                     "shape_id": 14,
#                     "shape_type": 17,
#                     "text": "Financial Research Agent",
#                     "x": 114127,
#                     "y": 53406,
#                     "width": 7836303,
#                     "height": 646331
#                 }
#             ],
#             "content": [],
#             "title": "Required capabilities"
#         },
#         {
#             "title": "Financial Research Agent\\u00a0\\u00a0",
#             "extra_shapes": [
#                 {
#                     "shape_id": 4,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 585540,
#                     "y": 1406236,
#                     "width": 11023848,
#                     "height": 4956464
#                 },
#                 {
#                     "shape_id": 6,
#                     "shape_type": 17,
#                     "text": "Researcher Experience\nGuided objective intake with quick-start templates and ticker awareness\nDynamic plan board that highlights approvals, dependencies, and agent status\nIn-line task injection so analysts can steer the workflow as market context shifts\n",
#                     "x": 1105283,
#                     "y": 1643705,
#                     "width": 4852169,
#                     "height": 1946687
#                 },
#                 {
#                     "shape_id": 12,
#                     "shape_type": 17,
#                     "text": "Data and Knowledge Fabric\nBlends Yahoo Finance MCP, FMP fundamentals, SEC filings, transcripts, and Azure OpenAI reasoning into each step\nCosmos-backed session memory preserves every action, artifact, and rationale for audits or replays\nSummarizer and report agents transform raw findings into executive-ready insights",
#                     "x": 1105283,
#                     "y": 3372600,
#                     "width": 4711480,
#                     "height": 1908215
#                 },
#                 {
#                     "shape_id": 21,
#                     "shape_type": 9,
                    
#                     "x": 5919254,
#                     "y": 1406236,
#                     "width": 0,
#                     "height": 4956464
#                 },
#                 {
#                     "shape_id": 22,
#                     "shape_type": 17,
#                     "text": "Platform integrations\nCopilot Studio (M365 SDK)",
#                     "x": 1105283,
#                     "y": 5475124,
#                     "width": 4852169,
#                     "height": 679673
#                 },
#                 {
#                     "shape_id": 23,
#                     "shape_type": 17,
#                     "text": "Agent Orchestration \\u000b(Modular, extensible, interoperable)\nReAct-inspired planner builds the research route and inserts human checkpoints\nSpecialist agents (company, SEC, earnings, fundamentals, technicals, forecast, synthesis) collaborate under a unified orchestrator\nReal-time execution view streams progress, exceptions, and final brief delivery\n",
#                     "x": 6404142,
#                     "y": 1643705,
#                     "width": 4852169,
#                     "height": 2469907
#                 },
#                 {
#                     "shape_id": 24,
#                     "shape_type": 17,
#                     "text": "Operational Guardrails\nIdentity-aware access and per-tenant isolation keep research data scoped to the right desk\nStructured telemetry and Application Insights traces deliver observability and governance\nConfigurable deployment scripts and environment controls ensure consistent rollouts across dev, pilot, and production\n",
#                     "x": 6404141,
#                     "y": 4334798,
#                     "width": 4852169,
#                     "height": 2187778
#                 },
#                 {
#                     "shape_id": 25,
#                     "shape_type": 9,
                    
#                     "x": 5919254,
#                     "y": 4317035,
#                     "width": 5687529,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 34,
#                     "shape_type": 9,
                    
#                     "x": 585540,
#                     "y": 3338286,
#                     "width": 5333714,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 36,
#                     "shape_type": 9,
                    
#                     "x": 585540,
#                     "y": 5340927,
#                     "width": 5333714,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 17,
#                     "text": "Our Approach",
#                     "x": 7649333,
#                     "y": 113860,
#                     "width": 3045171,
#                     "height": 523220
#                 }
#             ]
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 8,
#                     "shape_type": 17,
#                     "text": "Research Analyst",
#                     "x": -934522,
#                     "y": 3550885,
#                     "width": 3309013,
#                     "height": 307777
#                 },
#                 {
#                     "shape_id": 9,
#                     "shape_type": 17,
#                     "text": "UI/UX",
#                     "x": 1670282,
#                     "y": 3579624,
#                     "width": 635451,
#                     "height": 250298
#                 },
#                 {
#                     "shape_id": 10,
#                     "shape_type": 9,
                    
#                     "x": 1386297,
#                     "y": 2763118,
#                     "width": 283985,
#                     "height": 941655
#                 },
#                 {
#                     "shape_id": 17,
#                     "shape_type": 9,
                    
#                     "x": 1386297,
#                     "y": 3704773,
#                     "width": 283985,
#                     "height": 951971
#                 },
#                 {
#                     "shape_id": 33,
#                     "shape_type": 9,
                    
#                     "x": 1386297,
#                     "y": 3704773,
#                     "width": 283985,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 36,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 2410586,
#                     "y": 2231764,
#                     "width": 2863292,
#                     "height": 2085445
#                 },
#                 {
#                     "shape_id": 40,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6927173,
#                     "y": 2521422,
#                     "width": 1548630,
#                     "height": 1251633
#                 },
#                 {
#                     "shape_id": 1524,
#                     "shape_type": 17,
#                     "text": "Fundamental & Technical Agent",
#                     "x": 7099030,
#                     "y": 2582384,
#                     "width": 1204039,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 1530,
#                     "shape_type": 13,
                    
#                     "x": 7001790,
#                     "y": 2676950,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 1532,
#                     "shape_type": 17,
#                     "text": "Multi-Agent Host Orchestrator & Planner",
#                     "x": 2839777,
#                     "y": 2291388,
#                     "width": 2056859,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 1533,
#                     "shape_type": 13,
                    
#                     "x": 2634955,
#                     "y": 2387293,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 1545,
#                     "shape_type": 1,
#                     "text": "An intelligent multi-agent orchestrator that can generate plans from context and  delegate to remote specialist agents \\u000band human agents when required ",
#                     "x": 2461901,
#                     "y": 2886943,
#                     "width": 2760663,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1546,
#                     "shape_type": 1,
#                     "text": "A specialized agent to retrieve the fundamental and technical data",
#                     "x": 6981496,
#                     "y": 3045469,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1558,
#                     "shape_type": 1,
#                     "text": "API",
#                     "x": 6981057,
#                     "y": 3487053,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1561,
#                     "shape_type": 1,
#                     "text": "A2A/MCP",
#                     "x": 2461901,
#                     "y": 3416726,
#                     "width": 736540,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1562,
#                     "shape_type": 1,
#                     "text": "Multi-Agent Orchestration",
#                     "x": 3249755,
#                     "y": 3416726,
#                     "width": 1969799,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1563,
#                     "shape_type": 1,
#                     "text": "Human in the loop",
#                     "x": 2461900,
#                     "y": 3627459,
#                     "width": 1163305,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1564,
#                     "shape_type": 1,
#                     "text": "Inter-Agent Memory",
#                     "x": 3674246,
#                     "y": 3627459,
#                     "width": 1545308,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1565,
#                     "shape_type": 1,
#                     "text": "Evaluation",
#                     "x": 2461900,
#                     "y": 3838192,
#                     "width": 888413,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1566,
#                     "shape_type": 1,
#                     "text": "File Processing",
#                     "x": 3430505,
#                     "y": 3838192,
#                     "width": 888413,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1567,
#                     "shape_type": 1,
#                     "text": "Tools",
#                     "x": 4399110,
#                     "y": 3838192,
#                     "width": 820444,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1568,
#                     "shape_type": 1,
#                     "text": "Agent Registry",
#                     "x": 2461900,
#                     "y": 4043381,
#                     "width": 1087634,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1569,
#                     "shape_type": 1,
#                     "text": "Telemetry & Tracing",
#                     "x": 3627716,
#                     "y": 4043381,
#                     "width": 1591838,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 2,
#                     "shape_type": 17,
#                     "text": "Financial Research Agent - Architecture ",
#                     "x": 314132,
#                     "y": 151232,
#                     "width": 5610504,
#                     "height": 369332
#                 },
#                 {
#                     "shape_id": 26,
#                     "shape_type": 13,
                    
#                     "x": 8857251,
#                     "y": 1655871,
#                     "width": 712431,
#                     "height": 622190
#                 },
#                 {
#                     "shape_id": 13,
#                     "shape_type": 9,
                    
#                     "x": 5289087,
#                     "y": 834859,
#                     "width": 1640568,
#                     "height": 2711328
#                 },
#                 {
#                     "shape_id": 44,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6929655,
#                     "y": 297535,
#                     "width": 1477438,
#                     "height": 1074647
#                 },
#                 {
#                     "shape_id": 46,
#                     "shape_type": 17,
#                     "text": "Earnings\nAgent",
#                     "x": 7188008,
#                     "y": 352581,
#                     "width": 1314473,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 49,
#                     "shape_type": 13,
                    
#                     "x": 7004272,
#                     "y": 453063,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 51,
#                     "shape_type": 1,
#                     "text": "Earnings Calls Agent \\u2013 Call Transcript retrieval and analysis",
#                     "x": 6968350,
#                     "y": 709049,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 55,
#                     "shape_type": 1,
#                     "text": "API",
#                     "x": 6967109,
#                     "y": 1102233,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 3,
#                     "shape_type": 17,
#                     "text": "Mobile Web",
#                     "x": 746917,
#                     "y": 4768917,
#                     "width": 1028227,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 4,
#                     "shape_type": 5,
#                     "text": "",
#                     "x": 1153610,
#                     "y": 4561432,
#                     "width": 190500,
#                     "height": 190500
#                 },
#                 {
#                     "shape_id": 11,
#                     "shape_type": 17,
#                     "text": "Teams",
#                     "x": 907772,
#                     "y": 3785922,
#                     "width": 572038,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 14,
#                     "shape_type": 13,
                    
#                     "x": 1030820,
#                     "y": 3524494,
#                     "width": 305430,
#                     "height": 305428
#                 },
#                 {
#                     "shape_id": 16,
#                     "shape_type": 17,
#                     "text": "MCP/A2A via APIM",
#                     "x": 595936,
#                     "y": 2315501,
#                     "width": 1411330,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 23,
#                     "shape_type": 13,
                    
#                     "x": 1001284,
#                     "y": 2554574,
#                     "width": 363571,
#                     "height": 363571
#                 },
#                 {
#                     "shape_id": 45,
#                     "shape_type": 6,
                    
#                     "x": 10900637,
#                     "y": 1524633,
#                     "width": 429023,
#                     "height": 200055
#                 },
#                 {
#                     "shape_id": 1515,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6928414,
#                     "y": 1425174,
#                     "width": 1526816,
#                     "height": 1007674
#                 },
#                 {
#                     "shape_id": 1516,
#                     "shape_type": 17,
#                     "text": "Company Agent",
#                     "x": 7186767,
#                     "y": 1480219,
#                     "width": 1314473,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 1517,
#                     "shape_type": 1,
#                     "text": "Earnings Calls Agent \\u2013 Call Transcript retrieval and analysis",
#                     "x": 6982298,
#                     "y": 1645060,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1528,
#                     "shape_type": 1,
#                     "text": "MCP Client / Tools",
#                     "x": 6958224,
#                     "y": 2116154,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1529,
#                     "shape_type": 13,
                    
#                     "x": 6951631,
#                     "y": 1469615,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 1531,
#                     "shape_type": 9,
                    
#                     "x": 8452949,
#                     "y": 1952613,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1027,
#                     "shape_type": 9,
                    
#                     "x": 5289087,
#                     "y": 1929011,
#                     "width": 1639327,
#                     "height": 1617176
#                 },
#                 {
#                     "shape_id": 1031,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6937570,
#                     "y": 3861629,
#                     "width": 1548608,
#                     "height": 842122
#                 },
#                 {
#                     "shape_id": 1033,
#                     "shape_type": 17,
#                     "text": "Knowledge Agent",
#                     "x": 7109427,
#                     "y": 3922590,
#                     "width": 1204039,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 1035,
#                     "shape_type": 1,
#                     "text": "Custom Product Knowledgebase",
#                     "x": 6975144,
#                     "y": 4156052,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1036,
#                     "shape_type": 1,
#                     "text": "Vector Search",
#                     "x": 7010560,
#                     "y": 4465442,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1038,
#                     "shape_type": 6,
                    
#                     "x": 7007105,
#                     "y": 3948950,
#                     "width": 242855,
#                     "height": 242855
#                 },
#                 {
#                     "shape_id": 1046,
#                     "shape_type": 9,
                    
#                     "x": 8477044,
#                     "y": 3210408,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1047,
#                     "shape_type": 17,
#                     "text": "Approved",
#                     "x": 1609472,
#                     "y": 3000066,
#                     "width": 782749,
#                     "height": 202218
#                 },
#                 {
#                     "shape_id": 1048,
#                     "shape_type": 17,
#                     "text": "Denied",
#                     "x": 1619987,
#                     "y": 4003896,
#                     "width": 761721,
#                     "height": 182807
#                 },
#                 {
#                     "shape_id": 1049,
#                     "shape_type": 9,
                    
#                     "x": 1552550,
#                     "y": 3930376,
#                     "width": 850092,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1051,
#                     "shape_type": 9,
                    
#                     "x": 1538433,
#                     "y": 3264858,
#                     "width": 850092,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1056,
#                     "shape_type": 9,
                    
#                     "x": 3161720,
#                     "y": 4780693,
#                     "width": 926970,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1059,
#                     "shape_type": 6,
                    
#                     "x": 907772,
#                     "y": 5749913,
#                     "width": 10392338,
#                     "height": 1026276
#                 },
#                 {
#                     "shape_id": 1067,
#                     "shape_type": 13,
                    
#                     "x": 1020216,
#                     "y": 3033914,
#                     "width": 342830,
#                     "height": 342829
#                 },
#                 {
#                     "shape_id": 1069,
#                     "shape_type": 13,
                    
#                     "x": 1072226,
#                     "y": 4127678,
#                     "width": 307777,
#                     "height": 307782
#                 },
#                 {
#                     "shape_id": 1075,
#                     "shape_type": 9,
                    
#                     "x": 8496010,
#                     "y": 4231984,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1077,
#                     "shape_type": 9,
                    
#                     "x": 5260136,
#                     "y": 3147239,
#                     "width": 1667037,
#                     "height": 396235
#                 },
#                 {
#                     "shape_id": 1079,
#                     "shape_type": 9,
                    
#                     "x": 5266724,
#                     "y": 3543474,
#                     "width": 1670846,
#                     "height": 739216
#                 },
#                 {
#                     "shape_id": 1087,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6918441,
#                     "y": 4857465,
#                     "width": 1548608,
#                     "height": 842122
#                 },
#                 {
#                     "shape_id": 1540,
#                     "shape_type": 17,
#                     "text": "Other Agents",
#                     "x": 7090298,
#                     "y": 4918426,
#                     "width": 1204039,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 1541,
#                     "shape_type": 1,
#                     "text": "Forecaster, Summarizer, Report",
#                     "x": 6956015,
#                     "y": 5151888,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1549,
#                     "shape_type": 1,
#                     "text": "API",
#                     "x": 7010560,
#                     "y": 5465276,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1570,
#                     "shape_type": 9,
                    
#                     "x": 8468528,
#                     "y": 5253767,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1574,
#                     "shape_type": 13,
                    
#                     "x": 2839777,
#                     "y": 5300760,
#                     "width": 218605,
#                     "height": 218605
#                 },
#                 {
#                     "shape_id": 1575,
#                     "shape_type": 13,
                    
#                     "x": 9101938,
#                     "y": 3156200,
#                     "width": 231132,
#                     "height": 231132
#                 },
#                 {
#                     "shape_id": 1576,
#                     "shape_type": 13,
                    
#                     "x": 9097585,
#                     "y": 4150142,
#                     "width": 231132,
#                     "height": 231132
#                 },
#                 {
#                     "shape_id": 1577,
#                     "shape_type": 13,
                    
#                     "x": 9103115,
#                     "y": 5172342,
#                     "width": 231132,
#                     "height": 231132
#                 },
#                 {
#                     "shape_id": 1579,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway",
#                     "x": 8736194,
#                     "y": 3877961,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1581,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway",
#                     "x": 8716603,
#                     "y": 2875430,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1583,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway",
#                     "x": 8743749,
#                     "y": 4918760,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1587,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway\nMCP Server/Tools",
#                     "x": 8646737,
#                     "y": 1429436,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1588,
#                     "shape_type": 13,
                    
#                     "x": 9345970,
#                     "y": 4130339,
#                     "width": 264101,
#                     "height": 226644
#                 },
#                 {
#                     "shape_id": 1589,
#                     "shape_type": 13,
                    
#                     "x": 9356890,
#                     "y": 5176315,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1590,
#                     "shape_type": 13,
                    
#                     "x": 9570179,
#                     "y": 4130339,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1591,
#                     "shape_type": 13,
                    
#                     "x": 9326080,
#                     "y": 3137848,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1592,
#                     "shape_type": 13,
                    
#                     "x": 9390464,
#                     "y": 1830535,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1593,
#                     "shape_type": 17,
#                     "text": "Azure AI Search",
#                     "x": 9851533,
#                     "y": 3988885,
#                     "width": 1506513,
#                     "height": 295190
#                 },
#                 {
#                     "shape_id": 1594,
#                     "shape_type": 17,
#                     "text": "Data Provider API",
#                     "x": 9790465,
#                     "y": 3022295,
#                     "width": 1506513,
#                     "height": 295190
#                 },
#                 {
#                     "shape_id": 1595,
#                     "shape_type": 17,
#                     "text": "Yahoo Finance MCP\nServer",
#                     "x": 9706562,
#                     "y": 1756154,
#                     "width": 1621858,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1596,
#                     "shape_type": 17,
#                     "text": "CosmosDB, Sessions\nMemory",
#                     "x": 3095954,
#                     "y": 5262530,
#                     "width": 1548596,
#                     "height": 330713
#                 },
#                 {
#                     "shape_id": 1597,
#                     "shape_type": 13,
                    
#                     "x": 7004395,
#                     "y": 4931988,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 2048,
#                     "shape_type": 17,
#                     "text": "Enterprise API",
#                     "x": 9878471,
#                     "y": 4951165,
#                     "width": 1506513,
#                     "height": 295190
#                 },
#                 {
#                     "shape_id": 2049,
#                     "shape_type": 9,
                    
#                     "x": 5289087,
#                     "y": 3546187,
#                     "width": 1666928,
#                     "height": 1820240
#                 }
#             ]
#         },
#         {
#             "title": "Converging the two popular OSS frameworks",
#             "extra_shapes": [
#                 {
#                     "shape_id": 2,
#                     "shape_type": 6,
                    
#                     "x": 1614838,
#                     "y": 2567666,
#                     "width": 8946554,
#                     "height": 2918838
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 6,
                    
#                     "x": 10006959,
#                     "y": 4667386,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 9,
#                     "shape_type": 6,
                    
#                     "x": 9660005,
#                     "y": 4673461,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 14,
#                     "shape_type": 6,
                    
#                     "x": 4388001,
#                     "y": 4639034,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 17,
#                     "shape_type": 6,
                    
#                     "x": 4711948,
#                     "y": 4611656,
#                     "width": 374971,
#                     "height": 374971
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 6,
                    
#                     "x": 5086716,
#                     "y": 4639034,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 23,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 5768627,
#                     "y": 3420201,
#                     "width": 687501,
#                     "height": 682738
#                 },
#                 {
#                     "shape_id": 24,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 1267426,
#                     "y": 1573306,
#                     "width": 9657148,
#                     "height": 4114800
#                 },
#                 {
#                     "shape_id": 25,
#                     "shape_type": 17,
#                     "text": "Microsoft Agent Framework",
#                     "x": 4096224,
#                     "y": 1786506,
#                     "width": 4032305,
#                     "height": 682738
#                 }
#             ]
#         },
#         {
#             "title": "Multi-Agent Orchestration",
#             "text": [
#                 "Inherit advanced orchestration patterns from Microsoft Research\\u2019s AutoGen combined with Semantic Kernel\\u2019s durable workflow orhcestration. Prototype experimental patterns locally, then scale them confidently in production."
#             ],
#             "extra_shapes": [
#                 {
#                     "shape_id": 196,
#                     "shape_type": 6,
                    
#                     "x": 5068306,
#                     "y": 1341762,
#                     "width": 6931195,
#                     "height": 4174476
#                 }
#             ]
#         },
#         {
#             "title": "Tools and Extensibility",
#             "text": [
#                 "Functions, APIs, and MCP servers can all be turned into tools.\n\nOut-of-the-box integrations to common enterprise systems, databases, and SaaS APIs \\u2014 so developers don\\u2019t start from scratch.\n\nDevelopers can declaratively define agents in YAML and specify which tools require human approval."
#             ],
#             "extra_shapes": [
#                 {
#                     "shape_id": 68,
#                     "shape_type": 6,
                    
#                     "x": 4942438,
#                     "y": 1662929,
#                     "width": 7220683,
#                     "height": 3532141
#                 }
#             ]
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": -1,
#                     "y": 0,
#                     "width": 12267128,
#                     "height": 6858000
#                 },
#                 {
#                     "shape_id": 12,
#                     "shape_type": 13,
                    
#                     "x": 4991938,
#                     "y": 2355306,
#                     "width": 7200062,
#                     "height": 2147387
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 17,
#                     "text": "The sequential orchestration pattern chains AI agents in a predefined, linear order. Each agent processes the output from the previous agent in the sequence, which creates a pipeline of specialized transformations.\n\nThe sequential orchestration pattern solves problems that require step-by-step processing, where each stage builds on the previous stage.\\u00a0",
#                     "x": 588263,
#                     "y": 1636778,
#                     "width": 3821670,
#                     "height": 3847207
#                 }
#             ],
#             "title": "Sequential pattern"
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": -1,
#                     "y": 0,
#                     "width": 12280007,
#                     "height": 6858000
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 17,
#                     "text": "The concurrent orchestration pattern runs multiple AI agents simultaneously on the same task. This approach allows each agent to provide independent analysis or processing from its unique perspective or specialization.\n\nThis pattern addresses scenarios where you need diverse insights or approaches to the same problem.\\u00a0",
#                     "x": 588263,
#                     "y": 1636778,
#                     "width": 3821670,
#                     "height": 3847207
#                 },
#                 {
#                     "shape_id": 4,
#                     "shape_type": 13,
                    
#                     "x": 4807525,
#                     "y": 1402205,
#                     "width": 7694537,
#                     "height": 4053589
#                 }
#             ],
#             "title": "Concurrent pattern"
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": -1,
#                     "y": 0,
#                     "width": 12241370,
#                     "height": 6858000
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 17,
#                     "text": "The group chat orchestration pattern enables multiple agents to solve problems, make decisions, or validate work by participating in a shared conversation thread where they collaborate through discussion. \n\nThis pattern addresses scenarios that are best accomplished through group discussion to reach decisions.",
#                     "x": 588263,
#                     "y": 1636778,
#                     "width": 3821670,
#                     "height": 3847207
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 13,
                    
#                     "x": 5218336,
#                     "y": 808522,
#                     "width": 6864096,
#                     "height": 5419023
#                 }
#             ],
#             "title": "Group chat pattern "
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": -1,
#                     "y": 0,
#                     "width": 12144778,
#                     "height": 6858000
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 17,
#                     "text": "The handoff orchestration pattern enables dynamic delegation of tasks between specialized agents. Each agent can assess the task at hand and decide whether to handle it directly or transfer it to a more appropriate agent based on the context and requirements.\n\nThis pattern addresses scenarios where the optimal agent for a task isn't known upfront or where the task requirements become clear only during processing.",
#                     "x": 588262,
#                     "y": 1636778,
#                     "width": 3935611,
#                     "height": 3847207
#                 },
#                 {
#                     "shape_id": 4,
#                     "shape_type": 13,
                    
#                     "x": 4976260,
#                     "y": 1237519,
#                     "width": 7272388,
#                     "height": 4851248
#                 }
#             ],
#             "title": "Handoff pattern "
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": -1,
#                     "y": 0,
#                     "width": 12331971,
#                     "height": 6858000
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 17,
#                     "text": "The magentic orchestration pattern is designed for open-ended and complex problems that don't have a predetermined plan of approach. \n\nThe manager agent communicates directly with specialized agents to gather information as it builds and refines the task ledger",
#                     "x": 588262,
#                     "y": 1636778,
#                     "width": 3935611,
#                     "height": 3847207
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 13,
                    
#                     "x": 4976260,
#                     "y": 1093675,
#                     "width": 7355710,
#                     "height": 4670650
#                 }
#             ],
#             "title": "Magentic pattern "
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 3486812,
#                     "y": 1570305,
#                     "width": 5830808,
#                     "height": 2485192
#                 },
#                 {
#                     "shape_id": 1030,
#                     "shape_type": 13,
                    
#                     "x": 2656009,
#                     "y": 1442100,
#                     "width": 1707800,
#                     "height": 896595
#                 },
#                 {
#                     "shape_id": 1032,
#                     "shape_type": 13,
                    
#                     "x": 536900,
#                     "y": 4656129,
#                     "width": 815386,
#                     "height": 428078
#                 },
#                 {
#                     "shape_id": 1034,
#                     "shape_type": 13,
                    
#                     "x": 2541301,
#                     "y": 4623393,
#                     "width": 474742,
#                     "height": 474742
#                 },
#                 {
#                     "shape_id": 4,
#                     "shape_type": 13,
                    
#                     "x": 599511,
#                     "y": 5165328,
#                     "width": 690165,
#                     "height": 362335
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 13,
                    
#                     "x": 2123801,
#                     "y": 5043294,
#                     "width": 633401,
#                     "height": 633399
#                 },
#                 {
#                     "shape_id": 11,
#                     "shape_type": 17,
#                     "text": "Recommended \\u201cGolden Path\\u201d Architecture",
#                     "x": 394117,
#                     "y": 57998,
#                     "width": 6184799,
#                     "height": 430887
#                 },
#                 {
#                     "shape_id": 12,
#                     "shape_type": 17,
#                     "text": "Cosmos DB\\u000bThread storage",
#                     "x": 1360081,
#                     "y": 1913566,
#                     "width": 997004,
#                     "height": 346249
#                 },
#                 {
#                     "shape_id": 14,
#                     "shape_type": 17,
#                     "text": "Key vault\\u000bConnections",
#                     "x": 1350075,
#                     "y": 2497542,
#                     "width": 820738,
#                     "height": 346249
#                 },
#                 {
#                     "shape_id": 15,
#                     "shape_type": 17,
#                     "text": "Azure Storage\\u000bFile storage",
#                     "x": 1360081,
#                     "y": 3081518,
#                     "width": 865622,
#                     "height": 346249
#                 },
#                 {
#                     "shape_id": 16,
#                     "shape_type": 17,
#                     "text": "Azure AI Foundry\\u000bStandard setup",
#                     "x": 4008466,
#                     "y": 1675167,
#                     "width": 1620636,
#                     "height": 430887
#                 },
#                 {
#                     "shape_id": 29,
#                     "shape_type": 9,
                    
#                     "x": 2797515,
#                     "y": 2201408,
#                     "width": 260467,
#                     "height": 916890
#                 },
#                 {
#                     "shape_id": 36,
#                     "shape_type": 17,
#                     "text": "Bot Service\\u000bChannels",
#                     "x": 10035668,
#                     "y": 3363868,
#                     "width": 714939,
#                     "height": 384721
#                 },
#                 {
#                     "shape_id": 37,
#                     "shape_type": 17,
#                     "text": "BYO resources",
#                     "x": 697449,
#                     "y": 1485388,
#                     "width": 1160767,
#                     "height": 215444
#                 },
#                 {
#                     "shape_id": 38,
#                     "shape_type": 17,
#                     "text": "AI tool resources",
#                     "x": 672496,
#                     "y": 4299578,
#                     "width": 1367939,
#                     "height": 215444
#                 },
#                 {
#                     "shape_id": 40,
#                     "shape_type": 17,
#                     "text": "Grounding with Bing Search",
#                     "x": 3010293,
#                     "y": 4777097,
#                     "width": 1925102,
#                     "height": 184666
#                 },
#                 {
#                     "shape_id": 41,
#                     "shape_type": 17,
#                     "text": "Azure AI Search",
#                     "x": 1252849,
#                     "y": 4777097,
#                     "width": 1114874,
#                     "height": 184666
#                 },
#                 {
#                     "shape_id": 42,
#                     "shape_type": 17,
#                     "text": "Logic Apps",
#                     "x": 1264424,
#                     "y": 5235655,
#                     "width": 825507,
#                     "height": 184666
#                 },
#                 {
#                     "shape_id": 43,
#                     "shape_type": 17,
#                     "text": "Azure Functions",
#                     "x": 2748757,
#                     "y": 5235250,
#                     "width": 1149598,
#                     "height": 184666
#                 },
#                 {
#                     "shape_id": 44,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 7494834,
#                     "y": 2372524,
#                     "width": 1620636,
#                     "height": 1500643
#                 },
#                 {
#                     "shape_id": 45,
#                     "shape_type": 17,
#                     "text": "Models",
#                     "x": 8021879,
#                     "y": 2477059,
#                     "width": 601127,
#                     "height": 215444
#                 },
#                 {
#                     "shape_id": 46,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 5608337,
#                     "y": 2372524,
#                     "width": 1620636,
#                     "height": 1500643
#                 },
#                 {
#                     "shape_id": 47,
#                     "shape_type": 17,
#                     "text": "Agents",
#                     "x": 6134122,
#                     "y": 2480769,
#                     "width": 569067,
#                     "height": 215444
#                 },
#                 {
#                     "shape_id": 48,
#                     "shape_type": 13,
                    
#                     "x": 7697424,
#                     "y": 2901568,
#                     "width": 409027,
#                     "height": 409027
#                 },
#                 {
#                     "shape_id": 49,
#                     "shape_type": 13,
                    
#                     "x": 8133514,
#                     "y": 2901732,
#                     "width": 436017,
#                     "height": 436017
#                 },
#                 {
#                     "shape_id": 50,
#                     "shape_type": 13,
                    
#                     "x": 8642458,
#                     "y": 2959653,
#                     "width": 283561,
#                     "height": 283561
#                 },
#                 {
#                     "shape_id": 51,
#                     "shape_type": 13,
                    
#                     "x": 7952917,
#                     "y": 3372903,
#                     "width": 307068,
#                     "height": 270725
#                 },
#                 {
#                     "shape_id": 52,
#                     "shape_type": 13,
                    
#                     "x": 5950164,
#                     "y": 2776851,
#                     "width": 939308,
#                     "height": 939308
#                 },
#                 {
#                     "shape_id": 58,
#                     "shape_type": 9,
                    
#                     "x": 7228973,
#                     "y": 3122846,
#                     "width": 265861,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 1044,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 7928624,
#                     "y": 4291503,
#                     "width": 3735067,
#                     "height": 2103168
#                 },
#                 {
#                     "shape_id": 1026,
#                     "shape_type": 13,
                    
#                     "x": 11181063,
#                     "y": 5873635,
#                     "width": 699606,
#                     "height": 699606
#                 },
#                 {
#                     "shape_id": 1045,
#                     "shape_type": 17,
#                     "text": "Containers \n(Azure Container Apps, etc)",
#                     "x": 8926019,
#                     "y": 5903292,
#                     "width": 2228174,
#                     "height": 461665
#                 },
#                 {
#                     "shape_id": 1046,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 8146632,
#                     "y": 4489174,
#                     "width": 3266005,
#                     "height": 1205890
#                 },
#                 {
#                     "shape_id": 1057,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 3682225,
#                     "y": 2372524,
#                     "width": 1620636,
#                     "height": 1500643
#                 },
#                 {
#                     "shape_id": 1058,
#                     "shape_type": 17,
#                     "text": "Built-in AI tools",
#                     "x": 3860678,
#                     "y": 2467908,
#                     "width": 1257845,
#                     "height": 215444
#                 },
#                 {
#                     "shape_id": 1067,
#                     "shape_type": 9,
                    
#                     "x": 5302861,
#                     "y": 3122846,
#                     "width": 305476,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 1071,
#                     "shape_type": 17,
#                     "text": "Azure AI Search\\u000bFile search index",
#                     "x": 1350075,
#                     "y": 3665493,
#                     "width": 1078372,
#                     "height": 346249
#                 },
#                 {
#                     "shape_id": 1098,
#                     "shape_type": 6,
                    
#                     "x": 427422,
#                     "y": 1852109,
#                     "width": 997069,
#                     "height": 2245162
#                 },
#                 {
#                     "shape_id": 1079,
#                     "shape_type": 9,
                    
#                     "x": 549422,
#                     "y": 5811005,
#                     "width": 6994272,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 1086,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 2575857,
#                     "y": 1858878,
#                     "width": 221659,
#                     "height": 2172335
#                 },
#                 {
#                     "shape_id": 1099,
#                     "shape_type": 9,
                    
#                     "x": 5204327,
#                     "y": 4046419,
#                     "width": 988699,
#                     "height": 1243626
#                 },
#                 {
#                     "shape_id": 1100,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 5032643,
#                     "y": 4763313,
#                     "width": 171685,
#                     "height": 706959
#                 },
#                 {
#                     "shape_id": 1110,
#                     "shape_type": 9,
                    
#                     "x": 6703189,
#                     "y": 1319540,
#                     "width": 5379126,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 1118,
#                     "shape_type": 9,
                    
#                     "x": 9636026,
#                     "y": 4032217,
#                     "width": 4332,
#                     "height": 440613
#                 },
#                 {
#                     "shape_id": 1120,
#                     "shape_type": 17,
#                     "text": "Microsoft Agent Framework\\u000bMulti-agent orchestrator",
#                     "x": 9124869,
#                     "y": 4872224,
#                     "width": 1890283,
#                     "height": 677108
#                 },
#                 {
#                     "shape_id": 1121,
#                     "shape_type": 9,
                    
#                     "x": 7161934,
#                     "y": 5325438,
#                     "width": 669058,
#                     "height": 1300328
#                 },
#                 {
#                     "shape_id": 1128,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 5302651,
#                     "y": 4141450,
#                     "width": 196753,
#                     "height": 4187612
#                 },
#                 {
#                     "shape_id": 1134,
#                     "shape_type": 13,
                    
#                     "x": 4912304,
#                     "y": 6404748,
#                     "width": 316276,
#                     "height": 316276
#                 },
#                 {
#                     "shape_id": 1136,
#                     "shape_type": 17,
#                     "text": "MCP servers",
#                     "x": 5347896,
#                     "y": 6471166,
#                     "width": 958869,
#                     "height": 183440
#                 },
#                 {
#                     "shape_id": 1137,
#                     "shape_type": 13,
                    
#                     "x": 6367620,
#                     "y": 6400218,
#                     "width": 310549,
#                     "height": 325336
#                 },
#                 {
#                     "shape_id": 1138,
#                     "shape_type": 17,
#                     "text": "A2A Servers",
#                     "x": 6627498,
#                     "y": 6437829,
#                     "width": 1012442,
#                     "height": 275160
#                 },
#                 {
#                     "shape_id": 1142,
#                     "shape_type": 9,
                    
#                     "x": 6738344,
#                     "y": 3553478,
#                     "width": 1088598,
#                     "height": 1727976
#                 },
#                 {
#                     "shape_id": 1028,
#                     "shape_type": 13,
                    
#                     "x": 9102522,
#                     "y": 3294238,
#                     "width": 1075671,
#                     "height": 564727
#                 },
#                 {
#                     "shape_id": 1147,
#                     "shape_type": 9,
                    
#                     "x": 9623096,
#                     "y": 1042200,
#                     "width": 17262,
#                     "height": 2252038
#                 },
#                 {
#                     "shape_id": 1154,
#                     "shape_type": 17,
#                     "text": "External APIs\\u000bOpenAPI specs",
#                     "x": 3738973,
#                     "y": 6470553,
#                     "width": 950189,
#                     "height": 323165
#                 },
#                 {
#                     "shape_id": 1155,
#                     "shape_type": 13,
                    
#                     "x": 559319,
#                     "y": 6130294,
#                     "width": 335339,
#                     "height": 335338
#                 },
#                 {
#                     "shape_id": 1156,
#                     "shape_type": 13,
                    
#                     "x": 1587671,
#                     "y": 6058437,
#                     "width": 718581,
#                     "height": 479053
#                 },
#                 {
#                     "shape_id": 13,
#                     "shape_type": 17,
#                     "text": "SharePoint",
#                     "x": 2208749,
#                     "y": 6205630,
#                     "width": 1149598,
#                     "height": 184666
#                 },
#                 {
#                     "shape_id": 17,
#                     "shape_type": 17,
#                     "text": "Fabric",
#                     "x": 965203,
#                     "y": 6205630,
#                     "width": 1149598,
#                     "height": 184666
#                 },
#                 {
#                     "shape_id": 18,
#                     "shape_type": 9,
                    
#                     "x": 4133408,
#                     "y": 3894833,
#                     "width": 2031110,
#                     "height": 2334283
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 2432552,
#                     "y": 3873378,
#                     "width": 174435,
#                     "height": 4236234
#                 },
#                 {
#                     "shape_id": 26,
#                     "shape_type": 13,
                    
#                     "x": 3228956,
#                     "y": 6327330,
#                     "width": 432893,
#                     "height": 432893
#                 },
#                 {
#                     "shape_id": 28,
#                     "shape_type": 17,
#                     "text": "File search",
#                     "x": 4119594,
#                     "y": 2959653,
#                     "width": 705258,
#                     "height": 184666
#                 },
#                 {
#                     "shape_id": 30,
#                     "shape_type": 17,
#                     "text": "Code interpreter",
#                     "x": 3957659,
#                     "y": 3404533,
#                     "width": 1029128,
#                     "height": 169277
#                 },
#                 {
#                     "shape_id": 2,
#                     "shape_type": 6,
                    
#                     "x": 5417617,
#                     "y": 435024,
#                     "width": 4534647,
#                     "height": 654978
#                 },
#                 {
#                     "shape_id": 19,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 5773503,
#                     "y": 1708168,
#                     "width": 3304805,
#                     "height": 501165
#                 },
#                 {
#                     "shape_id": 21,
#                     "shape_type": 17,
#                     "text": "Observability",
#                     "x": 6877580,
#                     "y": 1853591,
#                     "width": 1073435,
#                     "height": 215444
#                 },
#                 {
#                     "shape_id": 57,
#                     "shape_type": 6,
                    
#                     "x": 10708456,
#                     "y": 57999,
#                     "width": 1236043,
#                     "height": 1191138
#                 },
#                 {
#                     "shape_id": 59,
#                     "shape_type": 17,
#                     "text": "3P agents",
#                     "x": 10965586,
#                     "y": 165719,
#                     "width": 795089,
#                     "height": 215444
#                 },
#                 {
#                     "shape_id": 60,
#                     "shape_type": 9,
                    
#                     "x": 11326478,
#                     "y": 1249137,
#                     "width": 0,
#                     "height": 3003386
#                 },
#                 {
#                     "shape_id": 23,
#                     "shape_type": 13,
                    
#                     "x": 8171754,
#                     "y": 4639529,
#                     "width": 1010136,
#                     "height": 1010136
#                 }
#             ]
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 3,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 600292,
#                     "y": 1518228,
#                     "width": 11018524,
#                     "height": 448305
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 1,
#                     "text": "a",
#                     "x": 600292,
#                     "y": 1966530,
#                     "width": 11018524,
#                     "height": 4782668
#                 },
#                 {
#                     "shape_id": 14,
#                     "shape_type": 17,
#                     "text": "Financial Research Agent",
#                     "x": 114127,
#                     "y": 53406,
#                     "width": 7836303,
#                     "height": 646331
#                 }
#             ],
#             "content": [],
#             "title": "Required capabilities"
#         },
#         {
#             "title": "Financial Research Agent\\u00a0\\u00a0",
#             "extra_shapes": [
#                 {
#                     "shape_id": 4,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 585540,
#                     "y": 1406236,
#                     "width": 11023848,
#                     "height": 4956464
#                 },
#                 {
#                     "shape_id": 6,
#                     "shape_type": 17,
#                     "text": "Researcher Experience\nGuided objective intake with quick-start templates and ticker awareness\nDynamic plan board that highlights approvals, dependencies, and agent status\nIn-line task injection so analysts can steer the workflow as market context shifts\n",
#                     "x": 1105283,
#                     "y": 1643705,
#                     "width": 4852169,
#                     "height": 1946687
#                 },
#                 {
#                     "shape_id": 12,
#                     "shape_type": 17,
#                     "text": "Data and Knowledge Fabric\nBlends Yahoo Finance MCP, FMP fundamentals, SEC filings, transcripts, and Azure OpenAI reasoning into each step\nCosmos-backed session memory preserves every action, artifact, and rationale for audits or replays\nSummarizer and report agents transform raw findings into executive-ready insights",
#                     "x": 1105283,
#                     "y": 3372600,
#                     "width": 4711480,
#                     "height": 1908215
#                 },
#                 {
#                     "shape_id": 21,
#                     "shape_type": 9,
                    
#                     "x": 5919254,
#                     "y": 1406236,
#                     "width": 0,
#                     "height": 4956464
#                 },
#                 {
#                     "shape_id": 22,
#                     "shape_type": 17,
#                     "text": "Platform integrations\nCopilot Studio (M365 SDK)",
#                     "x": 1105283,
#                     "y": 5475124,
#                     "width": 4852169,
#                     "height": 679673
#                 },
#                 {
#                     "shape_id": 23,
#                     "shape_type": 17,
#                     "text": "Agent Orchestration \\u000b(Modular, extensible, interoperable)\nReAct-inspired planner builds the research route and inserts human checkpoints\nSpecialist agents (company, SEC, earnings, fundamentals, technicals, forecast, synthesis) collaborate under a unified orchestrator\nReal-time execution view streams progress, exceptions, and final brief delivery\n",
#                     "x": 6404142,
#                     "y": 1643705,
#                     "width": 4852169,
#                     "height": 2469907
#                 },
#                 {
#                     "shape_id": 24,
#                     "shape_type": 17,
#                     "text": "Operational Guardrails\nIdentity-aware access and per-tenant isolation keep research data scoped to the right desk\nStructured telemetry and Application Insights traces deliver observability and governance\nConfigurable deployment scripts and environment controls ensure consistent rollouts across dev, pilot, and production\n",
#                     "x": 6404141,
#                     "y": 4334798,
#                     "width": 4852169,
#                     "height": 2187778
#                 },
#                 {
#                     "shape_id": 25,
#                     "shape_type": 9,
                    
#                     "x": 5919254,
#                     "y": 4317035,
#                     "width": 5687529,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 34,
#                     "shape_type": 9,
                    
#                     "x": 585540,
#                     "y": 3338286,
#                     "width": 5333714,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 36,
#                     "shape_type": 9,
                    
#                     "x": 585540,
#                     "y": 5340927,
#                     "width": 5333714,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 17,
#                     "text": "Our Approach",
#                     "x": 7649333,
#                     "y": 113860,
#                     "width": 3045171,
#                     "height": 523220
#                 }
#             ]
#         },
#         {
#             "title": "Converging the two popular OSS frameworks",
#             "extra_shapes": [
#                 {
#                     "shape_id": 2,
#                     "shape_type": 6,
                    
#                     "x": 1614838,
#                     "y": 2567666,
#                     "width": 8946554,
#                     "height": 2918838
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 6,
                    
#                     "x": 10006959,
#                     "y": 4667386,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 9,
#                     "shape_type": 6,
                    
#                     "x": 9660005,
#                     "y": 4673461,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 14,
#                     "shape_type": 6,
                    
#                     "x": 4388001,
#                     "y": 4639034,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 17,
#                     "shape_type": 6,
                    
#                     "x": 4711948,
#                     "y": 4611656,
#                     "width": 374971,
#                     "height": 374971
#                 },
#                 {
#                     "shape_id": 20,
#                     "shape_type": 6,
                    
#                     "x": 5086716,
#                     "y": 4639034,
#                     "width": 320214,
#                     "height": 320214
#                 },
#                 {
#                     "shape_id": 23,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 5768627,
#                     "y": 3420201,
#                     "width": 687501,
#                     "height": 682738
#                 },
#                 {
#                     "shape_id": 24,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 1267426,
#                     "y": 1573306,
#                     "width": 9657148,
#                     "height": 4114800
#                 },
#                 {
#                     "shape_id": 25,
#                     "shape_type": 17,
#                     "text": "Microsoft Agent Framework",
#                     "x": 4096224,
#                     "y": 1786506,
#                     "width": 4032305,
#                     "height": 682738
#                 }
#             ]
#         },
#         {
#             "title": "Multi-Agent Orchestration",
#             "text": [
#                 "Inherit advanced orchestration patterns from Microsoft Research\\u2019s AutoGen combined with Semantic Kernel\\u2019s durable workflow orhcestration. Prototype experimental patterns locally, then scale them confidently in production."
#             ],
#             "extra_shapes": [
#                 {
#                     "shape_id": 196,
#                     "shape_type": 6,
                    
#                     "x": 5068306,
#                     "y": 1341762,
#                     "width": 6931195,
#                     "height": 4174476
#                 }
#             ]
#         },
#         {
#             "extra_shapes": [
#                 {
#                     "shape_id": 8,
#                     "shape_type": 17,
#                     "text": "Research Analyst",
#                     "x": -934522,
#                     "y": 3550885,
#                     "width": 3309013,
#                     "height": 307777
#                 },
#                 {
#                     "shape_id": 9,
#                     "shape_type": 17,
#                     "text": "UI/UX",
#                     "x": 1670282,
#                     "y": 3579624,
#                     "width": 635451,
#                     "height": 250298
#                 },
#                 {
#                     "shape_id": 10,
#                     "shape_type": 9,
                    
#                     "x": 1386297,
#                     "y": 2763118,
#                     "width": 283985,
#                     "height": 941655
#                 },
#                 {
#                     "shape_id": 17,
#                     "shape_type": 9,
                    
#                     "x": 1386297,
#                     "y": 3704773,
#                     "width": 283985,
#                     "height": 951971
#                 },
#                 {
#                     "shape_id": 33,
#                     "shape_type": 9,
                    
#                     "x": 1386297,
#                     "y": 3704773,
#                     "width": 283985,
#                     "height": 0
#                 },
#                 {
#                     "shape_id": 36,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 2410586,
#                     "y": 2231764,
#                     "width": 2863292,
#                     "height": 2085445
#                 },
#                 {
#                     "shape_id": 40,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6927173,
#                     "y": 2521422,
#                     "width": 1548630,
#                     "height": 1251633
#                 },
#                 {
#                     "shape_id": 1524,
#                     "shape_type": 17,
#                     "text": "Fundamental & Technical Agent",
#                     "x": 7099030,
#                     "y": 2582384,
#                     "width": 1204039,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 1530,
#                     "shape_type": 13,
                    
#                     "x": 7001790,
#                     "y": 2676950,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 1532,
#                     "shape_type": 17,
#                     "text": "Multi-Agent Host Orchestrator & Planner",
#                     "x": 2839777,
#                     "y": 2291388,
#                     "width": 2056859,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 1533,
#                     "shape_type": 13,
                    
#                     "x": 2634955,
#                     "y": 2387293,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 1545,
#                     "shape_type": 1,
#                     "text": "An intelligent multi-agent orchestrator that can generate plans from context and  delegate to remote specialist agents \\u000band human agents when required ",
#                     "x": 2461901,
#                     "y": 2886943,
#                     "width": 2760663,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1546,
#                     "shape_type": 1,
#                     "text": "A specialized agent to retrieve the fundamental and technical data",
#                     "x": 6981496,
#                     "y": 3045469,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1558,
#                     "shape_type": 1,
#                     "text": "API",
#                     "x": 6981057,
#                     "y": 3487053,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1561,
#                     "shape_type": 1,
#                     "text": "A2A/MCP",
#                     "x": 2461901,
#                     "y": 3416726,
#                     "width": 736540,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1562,
#                     "shape_type": 1,
#                     "text": "Multi-Agent Orchestration",
#                     "x": 3249755,
#                     "y": 3416726,
#                     "width": 1969799,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1563,
#                     "shape_type": 1,
#                     "text": "Human in the loop",
#                     "x": 2461900,
#                     "y": 3627459,
#                     "width": 1163305,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1564,
#                     "shape_type": 1,
#                     "text": "Inter-Agent Memory",
#                     "x": 3674246,
#                     "y": 3627459,
#                     "width": 1545308,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1565,
#                     "shape_type": 1,
#                     "text": "Evaluation",
#                     "x": 2461900,
#                     "y": 3838192,
#                     "width": 888413,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1566,
#                     "shape_type": 1,
#                     "text": "File Processing",
#                     "x": 3430505,
#                     "y": 3838192,
#                     "width": 888413,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1567,
#                     "shape_type": 1,
#                     "text": "Tools",
#                     "x": 4399110,
#                     "y": 3838192,
#                     "width": 820444,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1568,
#                     "shape_type": 1,
#                     "text": "Agent Registry",
#                     "x": 2461900,
#                     "y": 4043381,
#                     "width": 1087634,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1569,
#                     "shape_type": 1,
#                     "text": "Telemetry & Tracing",
#                     "x": 3627716,
#                     "y": 4043381,
#                     "width": 1591838,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 2,
#                     "shape_type": 17,
#                     "text": "Financial Research Agent - Architecture ",
#                     "x": 314132,
#                     "y": 151232,
#                     "width": 5610504,
#                     "height": 369332
#                 },
#                 {
#                     "shape_id": 26,
#                     "shape_type": 13,
                    
#                     "x": 8857251,
#                     "y": 1655871,
#                     "width": 712431,
#                     "height": 622190
#                 },
#                 {
#                     "shape_id": 13,
#                     "shape_type": 9,
                    
#                     "x": 5289087,
#                     "y": 834859,
#                     "width": 1640568,
#                     "height": 2711328
#                 },
#                 {
#                     "shape_id": 44,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6929655,
#                     "y": 297535,
#                     "width": 1477438,
#                     "height": 1074647
#                 },
#                 {
#                     "shape_id": 46,
#                     "shape_type": 17,
#                     "text": "Earnings\nAgent",
#                     "x": 7188008,
#                     "y": 352581,
#                     "width": 1314473,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 49,
#                     "shape_type": 13,
                    
#                     "x": 7004272,
#                     "y": 453063,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 51,
#                     "shape_type": 1,
#                     "text": "Earnings Calls Agent \\u2013 Call Transcript retrieval and analysis",
#                     "x": 6968350,
#                     "y": 709049,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 55,
#                     "shape_type": 1,
#                     "text": "API",
#                     "x": 6967109,
#                     "y": 1102233,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 3,
#                     "shape_type": 17,
#                     "text": "Mobile Web",
#                     "x": 746917,
#                     "y": 4768917,
#                     "width": 1028227,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 4,
#                     "shape_type": 5,
#                     "text": "",
#                     "x": 1153610,
#                     "y": 4561432,
#                     "width": 190500,
#                     "height": 190500
#                 },
#                 {
#                     "shape_id": 11,
#                     "shape_type": 17,
#                     "text": "Teams",
#                     "x": 907772,
#                     "y": 3785922,
#                     "width": 572038,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 14,
#                     "shape_type": 13,
                    
#                     "x": 1030820,
#                     "y": 3524494,
#                     "width": 305430,
#                     "height": 305428
#                 },
#                 {
#                     "shape_id": 16,
#                     "shape_type": 17,
#                     "text": "MCP/A2A via APIM",
#                     "x": 595936,
#                     "y": 2315501,
#                     "width": 1411330,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 23,
#                     "shape_type": 13,
                    
#                     "x": 1001284,
#                     "y": 2554574,
#                     "width": 363571,
#                     "height": 363571
#                 },
#                 {
#                     "shape_id": 45,
#                     "shape_type": 6,
                    
#                     "x": 10900637,
#                     "y": 1524633,
#                     "width": 429023,
#                     "height": 200055
#                 },
#                 {
#                     "shape_id": 1515,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6928414,
#                     "y": 1425174,
#                     "width": 1526816,
#                     "height": 1007674
#                 },
#                 {
#                     "shape_id": 1516,
#                     "shape_type": 17,
#                     "text": "Company Agent",
#                     "x": 7186767,
#                     "y": 1480219,
#                     "width": 1314473,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 1517,
#                     "shape_type": 1,
#                     "text": "Earnings Calls Agent \\u2013 Call Transcript retrieval and analysis",
#                     "x": 6982298,
#                     "y": 1645060,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1528,
#                     "shape_type": 1,
#                     "text": "MCP Client / Tools",
#                     "x": 6958224,
#                     "y": 2116154,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1529,
#                     "shape_type": 13,
                    
#                     "x": 6951631,
#                     "y": 1469615,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 1531,
#                     "shape_type": 9,
                    
#                     "x": 8452949,
#                     "y": 1952613,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1027,
#                     "shape_type": 9,
                    
#                     "x": 5289087,
#                     "y": 1929011,
#                     "width": 1639327,
#                     "height": 1617176
#                 },
#                 {
#                     "shape_id": 1031,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6937570,
#                     "y": 3861629,
#                     "width": 1548608,
#                     "height": 842122
#                 },
#                 {
#                     "shape_id": 1033,
#                     "shape_type": 17,
#                     "text": "Knowledge Agent",
#                     "x": 7109427,
#                     "y": 3922590,
#                     "width": 1204039,
#                     "height": 415498
#                 },
#                 {
#                     "shape_id": 1035,
#                     "shape_type": 1,
#                     "text": "Custom Product Knowledgebase",
#                     "x": 6975144,
#                     "y": 4156052,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1036,
#                     "shape_type": 1,
#                     "text": "Vector Search",
#                     "x": 7010560,
#                     "y": 4465442,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1038,
#                     "shape_type": 6,
                    
#                     "x": 7007105,
#                     "y": 3948950,
#                     "width": 242855,
#                     "height": 242855
#                 },
#                 {
#                     "shape_id": 1046,
#                     "shape_type": 9,
                    
#                     "x": 8477044,
#                     "y": 3210408,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1047,
#                     "shape_type": 17,
#                     "text": "Approved",
#                     "x": 1609472,
#                     "y": 3000066,
#                     "width": 782749,
#                     "height": 202218
#                 },
#                 {
#                     "shape_id": 1048,
#                     "shape_type": 17,
#                     "text": "Denied",
#                     "x": 1619987,
#                     "y": 4003896,
#                     "width": 761721,
#                     "height": 182807
#                 },
#                 {
#                     "shape_id": 1049,
#                     "shape_type": 9,
                    
#                     "x": 1552550,
#                     "y": 3930376,
#                     "width": 850092,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1051,
#                     "shape_type": 9,
                    
#                     "x": 1538433,
#                     "y": 3264858,
#                     "width": 850092,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1056,
#                     "shape_type": 9,
                    
#                     "x": 3161720,
#                     "y": 4780693,
#                     "width": 926970,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1059,
#                     "shape_type": 6,
                    
#                     "x": 907772,
#                     "y": 5749913,
#                     "width": 10392338,
#                     "height": 1026276
#                 },
#                 {
#                     "shape_id": 1067,
#                     "shape_type": 13,
                    
#                     "x": 1020216,
#                     "y": 3033914,
#                     "width": 342830,
#                     "height": 342829
#                 },
#                 {
#                     "shape_id": 1069,
#                     "shape_type": 13,
                    
#                     "x": 1072226,
#                     "y": 4127678,
#                     "width": 307777,
#                     "height": 307782
#                 },
#                 {
#                     "shape_id": 1075,
#                     "shape_type": 9,
                    
#                     "x": 8496010,
#                     "y": 4231984,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1077,
#                     "shape_type": 9,
                    
#                     "x": 5260136,
#                     "y": 3147239,
#                     "width": 1667037,
#                     "height": 396235
#                 },
#                 {
#                     "shape_id": 1079,
#                     "shape_type": 9,
                    
#                     "x": 5266724,
#                     "y": 3543474,
#                     "width": 1670846,
#                     "height": 739216
#                 },
#                 {
#                     "shape_id": 1087,
#                     "shape_type": 1,
#                     "text": "",
#                     "x": 6918441,
#                     "y": 4857465,
#                     "width": 1548608,
#                     "height": 842122
#                 },
#                 {
#                     "shape_id": 1540,
#                     "shape_type": 17,
#                     "text": "Other Agents",
#                     "x": 7090298,
#                     "y": 4918426,
#                     "width": 1204039,
#                     "height": 253916
#                 },
#                 {
#                     "shape_id": 1541,
#                     "shape_type": 1,
#                     "text": "Forecaster, Summarizer, Report",
#                     "x": 6956015,
#                     "y": 5151888,
#                     "width": 1439984,
#                     "height": 429077
#                 },
#                 {
#                     "shape_id": 1549,
#                     "shape_type": 1,
#                     "text": "API",
#                     "x": 7010560,
#                     "y": 5465276,
#                     "width": 1439984,
#                     "height": 165704
#                 },
#                 {
#                     "shape_id": 1570,
#                     "shape_type": 9,
                    
#                     "x": 8468528,
#                     "y": 5253767,
#                     "width": 475650,
#                     "height": 1
#                 },
#                 {
#                     "shape_id": 1574,
#                     "shape_type": 13,
                    
#                     "x": 2839777,
#                     "y": 5300760,
#                     "width": 218605,
#                     "height": 218605
#                 },
#                 {
#                     "shape_id": 1575,
#                     "shape_type": 13,
                    
#                     "x": 9101938,
#                     "y": 3156200,
#                     "width": 231132,
#                     "height": 231132
#                 },
#                 {
#                     "shape_id": 1576,
#                     "shape_type": 13,
                    
#                     "x": 9097585,
#                     "y": 4150142,
#                     "width": 231132,
#                     "height": 231132
#                 },
#                 {
#                     "shape_id": 1577,
#                     "shape_type": 13,
                    
#                     "x": 9103115,
#                     "y": 5172342,
#                     "width": 231132,
#                     "height": 231132
#                 },
#                 {
#                     "shape_id": 1579,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway",
#                     "x": 8736194,
#                     "y": 3877961,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1581,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway",
#                     "x": 8716603,
#                     "y": 2875430,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1583,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway",
#                     "x": 8743749,
#                     "y": 4918760,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1587,
#                     "shape_type": 17,
#                     "text": "Gen-AI Gateway\nMCP Server/Tools",
#                     "x": 8646737,
#                     "y": 1429436,
#                     "width": 1398467,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1588,
#                     "shape_type": 13,
                    
#                     "x": 9345970,
#                     "y": 4130339,
#                     "width": 264101,
#                     "height": 226644
#                 },
#                 {
#                     "shape_id": 1589,
#                     "shape_type": 13,
                    
#                     "x": 9356890,
#                     "y": 5176315,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1590,
#                     "shape_type": 13,
                    
#                     "x": 9570179,
#                     "y": 4130339,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1591,
#                     "shape_type": 13,
                    
#                     "x": 9326080,
#                     "y": 3137848,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1592,
#                     "shape_type": 13,
                    
#                     "x": 9390464,
#                     "y": 1830535,
#                     "width": 243602,
#                     "height": 243602
#                 },
#                 {
#                     "shape_id": 1593,
#                     "shape_type": 17,
#                     "text": "Azure AI Search",
#                     "x": 9851533,
#                     "y": 3988885,
#                     "width": 1506513,
#                     "height": 295190
#                 },
#                 {
#                     "shape_id": 1594,
#                     "shape_type": 17,
#                     "text": "Data Provider API",
#                     "x": 9790465,
#                     "y": 3022295,
#                     "width": 1506513,
#                     "height": 295190
#                 },
#                 {
#                     "shape_id": 1595,
#                     "shape_type": 17,
#                     "text": "Yahoo Finance MCP\nServer",
#                     "x": 9706562,
#                     "y": 1756154,
#                     "width": 1621858,
#                     "height": 360000
#                 },
#                 {
#                     "shape_id": 1596,
#                     "shape_type": 17,
#                     "text": "CosmosDB, Sessions\nMemory",
#                     "x": 3095954,
#                     "y": 5262530,
#                     "width": 1548596,
#                     "height": 330713
#                 },
#                 {
#                     "shape_id": 1597,
#                     "shape_type": 13,
                    
#                     "x": 7004395,
#                     "y": 4931988,
#                     "width": 226366,
#                     "height": 226366
#                 },
#                 {
#                     "shape_id": 2048,
#                     "shape_type": 17,
#                     "text": "Enterprise API",
#                     "x": 9878471,
#                     "y": 4951165,
#                     "width": 1506513,
#                     "height": 295190
#                 },
#                 {
#                     "shape_id": 2049,
#                     "shape_type": 9,
                    
#                     "x": 5289087,
#                     "y": 3546187,
#                     "width": 1666928,
#                     "height": 1820240
#                 },
#                 {
#                     "shape_id": 5,
#                     "shape_type": 13,
                    
#                     "x": 5467884,
#                     "y": 3293362,
#                     "width": 231132,
#                     "height": 231132
#                 }
#             ]
#         }
#     ]
# }
    
#     json_data = {
#     "template": "/code/app/templates/template.pptx",
#     "slides": [
#         {
#             "title": "Star Wars is Cool"
#         },
#         {
#             "agenda": [
#                 "Introduction",
#                 "What makes Star Wars cool?",
#                 "Iconic characters & ships",
#                 "Star Wars art & fandom",
#                 "Conclusion"
#             ]
#         },
#         {
#             "title": "Introduction - The Star Wars Universe",
#             "pictures": [
#                 "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80"
#             ]
#         },
#         {
#             "sectionname": "What Makes Star Wars Cool?"
#         },
#         {
#             "title": "Why Fans Love Star Wars",
#             "content": "Star Wars combines epic storytelling, creative world-building, memorable characters, and legendary battles between good and evil. Its influence spans movies, TV, games, art, and more.",
#             "pictures": [
#                 "https://lumiere-a.akamaihd.net/v1/images/607598d0230e6a00018e21b2-image_354b1b56.jpeg?region=0%2C48%2C1536%2C768"
#             ]
#         },
#         {
#             "title": "Iconic Characters & Ships",
#             "content": "Star Wars is renowned for its legendary cast: Luke Skywalker, Darth Vader, Princess Leia, Yoda, and more. The Millennium Falcon, X-Wings, and Star Destroyers are pop-culture icons.",
#             "tables": [
#                 {
#                     "headers": ["Character", "Role", "First Appearance"],
#                     "rows": [
#                         ["Luke Skywalker", "Hero", "A New Hope"],
#                         ["Darth Vader", "Villain", "A New Hope"],
#                         ["Princess Leia", "Rebel Leader", "A New Hope"]
#                     ]
#                 }
#             ]
#         },
#         {
#             "thanks": "Thank you for celebrating Star Wars!",
#             "contactinfo": "Test Bot\n- test@nothing.com\n- 555-123-4567"
#         }
#     ]
# }
    response = requests.post(url, json=json_data)
    if response.status_code == 200:
        # with open("generated_presentation.pptx", "wb") as f:
        #     f.write(response.content)
        # print("PPTX file saved as generated_presentation.pptx")
        print(response.json())
    else:
        print(f"Failed to generate PPTX. Status code: {response.status_code}, Response: {response.text}")



def parse():
    # upload generated_presentation.pptx to the server and see if it can be parsed
    url = "http://localhost:8888/parse"
    #with open("generated_presentation.pptx", "rb") as f:
    with open("FinAgent.pptx", "rb") as f:
        files = {"file": ("generated_presentation.pptx", f, "application/vnd.openxmlformats-officedocument.presentationml.presentation")}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("PPTX file parsed successfully.")
            print(response.json())
        else:
            print(f"Failed to parse PPTX. Status code: {response.status_code}, Response: {response.text}")

def main():
    generate()
    #parse()

if __name__ == "__main__":
    main()