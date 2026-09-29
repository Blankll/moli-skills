# SOURCES — 词库来源与维护记录

词库词条的可追溯来源。**只合入 license 兼容(MIT / Apache-2.0)的来源**;无 license 的仓库(如 funNLP)只作参考,不直接复用。

## 开源词库来源

| 来源 | License | 取材范围 | 合入时间 |
|---|---|---|---|
| [edwardxckf/xiaohongshu-rules](https://github.com/edwardxckf/xiaohongshu-rules) `banned-words.txt`(411 词) | MIT | 极限词变体、医疗功效组、引流变体、金融承诺;社区规范全文另存于 `platform-rules/` | 2026.09 |
| [konsheng/Sensitive-lexicon](https://github.com/konsheng/Sensitive-lexicon) `Vocabulary/广告类型.txt`(123 词) | MIT | 站外平台提及(淘宝/京东/抖音等)、引流变体;其余为电商过滤词,未采用 | 2026.09 |

导入方式:见 `scripts/import_wordlist.py` —— 词面对齐与去重由脚本完成,类别/严重度/替换建议逐条人工(或 Agent 复核)确定后再入 TSV。

## 有意不入库的词(及理由)

导入时主动排除,后续刷新时同样跳过:

- **审核类词**(赌博器械/毒品/色情/诈骗暗语,如枪支、大麻、杀猪盘、换妻):属内容审核问题,不是营销合规问题;正常创作者文案中不出现,入库只会制造无意义告警
- **误报率过高的泛词**(第一、高效、大牌、内分泌、失眠、绝对值 等):在个人记录、科普、数码参数等合法语境中极高频;"第一"会命中"第一次用","高效"会命中"高效清洁"。具体的高风险组合(全网第一、增强免疫力)已单独收录
- **场景依赖词**(老字号、招财、秒杀、兼职):降级为 `caution`,由 L3 上下文判断兜底,而非直接拒绝

## 官方规则(权威锚点)

词库永远滞后于平台规则,L3 上下文判断以官方文件为准:

- 《广告法》全文 — [国家市场监督管理总局](https://www.samr.gov.cn/) / [全国人大网](http://www.npc.gov.cn/)
- 小红书《社区规范》— 官方页面(2021-12 快照已存 `platform-rules/xiaohongshu-community-guidelines-2021.txt`)
- 微信《公众平台运营规范》— <https://mp.weixin.qq.com> (运营规范页)
- 抖音《社区自律公约》— <https://www.douyin.com/rules>

## 行业工具(交叉验证用)

词库不开放,用于发布前抽样比对、发现漏检:

| 工具 | 覆盖 |
|---|---|
| [零克查词](https://www.lingkechaci.com) | 小红书/抖音/B站/快手,创作者圈常用,更新快 |
| [句无忧](https://www.check51.com) | 按行业与平台定向查 |
| [词爪网](https://www.cizhua.com) | 20+ 行业细分词库 |
| [站长工具·广告法检测](https://stool.chinaz.com/vabkeywords) | 电商/地产/医疗/化妆品文案 |

## 刷新流程

1. 下载目标来源词表 → `python3 scripts/import_wordlist.py --source <词表> --platform <平台>` 生成待审草稿
2. 逐条补全 类别/严重度/替换建议;对照上文"有意不入库"清单排除
3. 复制进对应 TSV,更新文件头 `version:` 注释,并在本文件登记来源
4. 跑 `detect.py` 回归:确保退出码与新词条匹配正常
