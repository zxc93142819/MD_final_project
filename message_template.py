
main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/4HFOPeR.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "功能介紹與使用說明",
              "text": "功能介紹與使用說明"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://img.ixintu.com/download/jpg/20201115/a5671772e12fb2d62caf05232e4d75ba_512_512.jpg!con",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "選擇衛教文章類別",
              "text": "選擇衛教文章類別"
            },
            "height": "md",
            "color": "#ff6666",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://img.ixintu.com/download/jpg/20210110/90acedef80e3c31c610cdb43a555a424_512_512.jpg!bg",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我的瀏覽紀錄",
              "text": "查看我的瀏覽紀錄"
            },
            "height": "md",
            "color": "#ff66b3",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
  ]
}

show_pic = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/dWyXPt9.png",
        "aspectMode": "fit",
        "size": "full",
        "aspectRatio": "2:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "前往網頁看圖片",
              "uri": "https://i.imgur.com/dWyXPt9.png"
            },
            "height": "md",
            "color": "#5cd65c",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回主選單",
              "text": "主選單"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

no_result = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查無記錄哦~",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

introduction_message = {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "功能介紹",
        "weight": "bold",
        "size": "lg",
        "margin": "lg",
        "align": "center"
      },
      {
        "type": "text",
        "text": "1. 依據您選擇的想看的衛教類別，給予您該類別下的主題",
        "wrap": True
      },
      {
        "type": "text",
        "text": "2. 選擇主題後，可以選擇語音或文字呈現",
        "wrap": True
      },
      {
        "type": "text",
        "text": "3. 點選我的瀏覽紀錄能看到自己之前有留下紀錄的查詢資料(最多10個)",
        "wrap": True
      },
      {
        "type": "text",
        "text": "使用說明",
        "weight": "bold",
        "size": "lg",
        "margin": "lg",
        "align": "center"
      },
      {
        "type": "text",
        "text": "◎　輸入「主選單」來開始所有操作",
        "wrap": True
      },
      {
        "type": "text",
        "text": "　　(也可由下方列選單點選快捷鍵)",
        "wrap": True
      },
      {
        "type": "text",
        "text": "◎　其餘依照按鈕提示進行點選即可",
        "wrap": True
      },
      {
        "type": "text",
        "text": "◎　操作時請拖曳後橫向(左右)滑動以查看更多呦~",
        "wrap": True
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

restaurant_item = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Brown Cafe",
          "weight": "bold",
          "size": "xl",
          "flex":1
        },
        {#["body"]["contents"][1]
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {#["body"]["contents"][1]["contents"][0]
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "店家評價",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "4.0",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "店家地址",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "營業時間",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": " ",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "查看店家",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "加入最愛",
            "uri": "http://linecorp.com/"
          },
          "style": "link",
          "height": "sm"
        }
      ],
      "flex": 0
    },
}

no_favorite = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "沒有最愛店家哦~~",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

favorite_item = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Brown Cafe",
          "weight": "bold",
          "size": "xl"
        },
        {#["body"]["contents"][1]
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {#["body"]["contents"][1]["contents"][0]
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "店家評價",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "4.0",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "店家地址",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "營業時間",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "10:00 - 23:00",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "查看店家",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        },
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "postback",
            "label": "從我的最愛移除",
            "data": "hello",
          }
        }
      ],
      "flex": 0
    },
}

first_item = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl",
        "wrap":True,
        "flex":1
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": " ",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": " ",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": " ",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": " ",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": " ",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": " ",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        },
        "height": "md",
        "color": "#00cc66",
        "style": "primary"
      }
    ],
    "flex": 0
  }
}

category_menu = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "選擇衛教文章類別",
        "weight": "bold",
        "align": "center"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "內科",
          "text": "內科"
        },
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "外科",
          "text": "外科"
        },
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "其他",
          "text": "其他"
        },
      },
      {
        "type": "separator"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單重新選擇功能",
          "text": "返回主選單重新選擇功能"
        },
      }
    ],
    "flex": 0
  }
}

article_list = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "選擇您想了解的文章",
        "weight": "bold",
        "align": "center"
      },
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回重新選擇衛教類別",
          "text": "返回重新選擇衛教類別"
        },
      }
    ],
    "flex": 0
  }
}

word_or_speak = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "選擇展示衛教文章方式",
        "weight": "bold",
        "align": "center"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "文章檔案",
          "text": "文章檔案"
        },
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "語音合成講給您聽",
          "text": "語音合成講給我聽"
        },
      },
      {
        "type": "separator"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "返回重新選擇我要的文章",
          "text": "返回重新選擇我要的文章"
        },
      }
    ],
    "flex": 0
  }
}

word_demo = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "您要的文章",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      },
      {
        "type": "button",
        "style": "link",
        "action": {
          "type": "uri",
          "label": "hello",
          "uri": "https://linecorp.com"
        }
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回重新選擇我要的文章表現方式",
          "text": "返回重新選擇我要的文章表現方式"
        },
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "postback",
          "label": "紀錄這次查詢",
          "data": "hello",
        },
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

article_template = {
  "type": "button",
  "style": "link",
  "height": "sm",
  "action": {
    "type": "message",
    "label": "文章標題",
    "text": "文章標題"
  },
}

separator = {
  "type": "separator"
}

add_reply = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查無相關店家",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      },
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

delete_reply = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查無相關店家",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回我的最愛清單",
          "text": "返回我的最愛清單"
        }
      },
      {
        "type" : "separator"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      },
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}


choose_chinese_or_taiwanese = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "選擇語音朗讀衛教文章的語言",
        "weight": "bold",
        "align": "center"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "中文",
          "text": "中文"
        },
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "台語",
          "text": "台語"
        },
      },
      {
        "type": "separator"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "返回重新選擇我要的文章表現方式",
          "text": "返回重新選擇我要的文章表現方式"
        },
      }
    ],
    "flex": 0
  }
}

restaurant_list = {
  "type": "carousel",
  "contents": [
      {
        "type": "bubble",
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "button",
              "style": "link",
              "action": {
                "type": "uri",
                "label": "hello",
                "uri": "https://linecorp.com"
              }
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "button",
              "style": "primary",
              "height": "sm",
              "action": {
                "type": "postback",
                "label": "從我的記錄移除",
                "data": "hello"
              }
            },
            {
              "type": "button",
              "style": "primary",
              "height": "sm",
              "action": {
                "type": "message",
                "label": "返回主選單",
                "text": "主選單"
              }
            }
          ],
        }
      }
  ]
}

show_restaurant_item = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "action": {
          "type": "uri",
          "label": "hello",
          "uri": "https://linecorp.com"
        }
      },
      {
        "type": "separator"
      },
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "從我的記錄移除",
          "data": "hello"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ],
  }
}
