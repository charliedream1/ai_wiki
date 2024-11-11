# 问题

No such file or directory: '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/models/MFD/weights.pt'


# 解决方案

参考：https://github.com/opendatalab/MinerU/issues/901

版本问题，把magic-pdf升级到最新版 0.9.x就可以了，0.9对应的模型仓库和0.8的不一样

如果接着报错：

```bash
2024-11-08 12:56:33.148 | ERROR | magic_pdf.tools.cli:parse_doc:109 - Missing key length_aware
full_key: model.model_config.length_aware
object_type=dict

Traceback (most recent call last):

File "/home/lh1121871443/anaconda3/envs/MinerU/bin/magic-pdf", line 8, in
sys.exit(cli())
│ │ └
│ └
└ <module 'sys' (built-in)>
File "/home/lh1121871443/.local/lib/python3.10/site-packages/click/core.py", line 1157, in call
return self.main(*args, **kwargs)
│ │ │ └ {}
│ │ └ ()
│ └ <function BaseCommand.main at 0x7390fa73a290>
└
File "/home/lh1121871443/.local/lib/python3.10/site-packages/click/core.py", line 1078, in main
rv = self.invoke(ctx)
│ │ └ <click.core.Context object at 0x7390fb35e5c0>
│ └ <function Command.invoke at 0x7390fa73ad40>
└
File "/home/lh1121871443/.local/lib/python3.10/site-packages/click/core.py", line 1434, in invoke
return ctx.invoke(self.callback, **ctx.params)
│ │ │ │ │ └ {'path': '/home/lh1121871443/MinerU/demo/small_ocr.pdf', 'output_dir': './output', 'method': 'auto', 'lang': None, 'debug_abl...
│ │ │ │ └ <click.core.Context object at 0x7390fb35e5c0>
│ │ │ └ <function cli at 0x738fa7ee6b90>
│ │ └
│ └ <function Context.invoke at 0x7390fa739ab0>
└ <click.core.Context object at 0x7390fb35e5c0>
File "/home/lh1121871443/.local/lib/python3.10/site-packages/click/core.py", line 783, in invoke
return __callback(*args, **kwargs)
│ └ {'path': '/home/lh1121871443/MinerU/demo/small_ocr.pdf', 'output_dir': './output', 'method': 'auto', 'lang': None, 'debug_abl...
└ ()
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/tools/cli.py", line 115, in cli
parse_doc(path)
│ └ '/home/lh1121871443/MinerU/demo/small_ocr.pdf'
└ <function cli..parse_doc at 0x7390fa954040>

File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/tools/cli.py", line 96, in parse_doc
do_parse(
└ <function do_parse at 0x738fa7ee6290>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/tools/common.py", line 87, in do_parse
pipe.pipe_analyze()
│ └ <function UNIPipe.pipe_analyze at 0x738fa7ee6440>
└ <magic_pdf.pipe.UNIPipe.UNIPipe object at 0x738fa7cf80a0>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/pipe/UNIPipe.py", line 37, in pipe_analyze
self.model_list = doc_analyze(self.pdf_bytes, ocr=True,
│ │ │ │ └ b'%PDF-1.7\r\n%\xa1\xb3\xc5\xd7\r\n1 0 obj\r\n<</Pages 2 0 R /Type/Catalog>>\r\nendobj\r\n2 0 obj\r\n<</Count 8/Kids[ 4 0 R ...
│ │ │ └ <magic_pdf.pipe.UNIPipe.UNIPipe object at 0x738fa7cf80a0>
│ │ └ <function doc_analyze at 0x738fa81505e0>
│ └ []
└ <magic_pdf.pipe.UNIPipe.UNIPipe object at 0x738fa7cf80a0>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/doc_analyze_by_custom_model.py", line 147, in doc_analyze
custom_model = model_manager.get_model(ocr, show_log, lang, layout_model, formula_enable, table_enable)
│ │ │ │ │ │ │ └ None
│ │ │ │ │ │ └ None
│ │ │ │ │ └ None
│ │ │ │ └ None
│ │ │ └ False
│ │ └ True
│ └ <function ModelSingleton.get_model at 0x738fa8150550>
└ <magic_pdf.model.doc_analyze_by_custom_model.ModelSingleton object at 0x738fa7cf8eb0>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/doc_analyze_by_custom_model.py", line 75, in get_model
self._models[key] = custom_model_init(ocr=ocr, show_log=show_log, lang=lang, layout_model=layout_model,
│ │ │ │ │ │ │ └ None
│ │ │ │ │ │ └ None
│ │ │ │ │ └ False
│ │ │ │ └ True
│ │ │ └ <function custom_model_init at 0x738fa8150430>
│ │ └ (True, False, None, None, None, None)
│ └ {}
└ <magic_pdf.model.doc_analyze_by_custom_model.ModelSingleton object at 0x738fa7cf8eb0>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/doc_analyze_by_custom_model.py", line 126, in custom_model_init
custom_model = CustomPEKModel(**model_input)
│ └ {'ocr': True, 'show_log': False, 'models_dir': '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/mo...
└ <class 'magic_pdf.model.pdf_extract_kit.CustomPEKModel'>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/pdf_extract_kit.py", line 261, in init
self.mfr_model, self.mfr_transform = atom_model_manager.get_atom_model(
│ │ │ └ <function AtomModelSingleton.get_atom_model at 0x738e5437b520>
│ │ └ <magic_pdf.model.pdf_extract_kit.AtomModelSingleton object at 0x738e5433f130>
│ └ <magic_pdf.model.pdf_extract_kit.CustomPEKModel object at 0x738fa7cf8c10>
└ <magic_pdf.model.pdf_extract_kit.CustomPEKModel object at 0x738fa7cf8c10>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/pdf_extract_kit.py", line 131, in get_atom_model
self._models[key] = atom_model_init(model_name=atom_model_name, **kwargs)
│ │ │ │ │ └ {'mfr_weight_dir': '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/models/MFR/unimernet_small', '...
│ │ │ │ └ 'mfr'
│ │ │ └ <function atom_model_init at 0x738e5437b250>
│ │ └ ('mfr', None, None)
│ └ {('mfd', None, None): YOLO(
│ (model): DetectionModel(
│ (model): Sequential(
│ (0): Conv(
│ (conv): Conv2d(3, 64...
└ <magic_pdf.model.pdf_extract_kit.AtomModelSingleton object at 0x738e5433f130>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/pdf_extract_kit.py", line 153, in atom_model_init
atom_model = mfr_model_init(
└ <function mfr_model_init at 0x738e5437b010>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/magic_pdf/model/pdf_extract_kit.py", line 72, in mfr_model_init
model = task.build_model(cfg)
│ │ └ <unimernet.common.config.Config object at 0x738e540f7fd0>
│ └ <function BaseTask.build_model at 0x738f7d3cab90>
└ <unimernet.tasks.unimernet_train.UniMERNet_Train object at 0x738e540f7e20>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/unimernet/tasks/base_task.py", line 33, in build_model
return model_cls.from_config(model_config)
│ │ └ {'arch': 'unimernet', 'load_finetuned': False, 'load_pretrained': True, 'pretrained': '/home/lh1121871443/.cache/modelscope/h...
│ └ <classmethod(<function UniMERModel.from_config at 0x738f7d34c0d0>)>
└ <class 'unimernet.models.unimernet.unimernet.UniMERModel'>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/unimernet/models/unimernet/unimernet.py", line 102, in from_config
model = cls(
└ <class 'unimernet.models.unimernet.unimernet.UniMERModel'>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/unimernet/models/unimernet/unimernet.py", line 41, in init
length_aware=model_config.length_aware,
└ {'max_seq_len': 1536, 'model_name': '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/models/MFR/un...
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/dictconfig.py", line 355, in getattr
self._format_and_raise(
│ └ <function Node._format_and_raise at 0x738f957d0160>
└ {'max_seq_len': 1536, 'model_name': '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/models/MFR/un...
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/base.py", line 231, in _format_and_raise
format_and_raise(
└ <function format_and_raise at 0x738f957beef0>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/_utils.py", line 899, in format_and_raise
_raise(ex, cause)
│ │ └ ConfigKeyError('Missing key length_aware')
│ └ ConfigAttributeError('Missing key length_aware\n full_key: model.model_config.length_aware\n object_type=dict')
└ <function _raise at 0x738f957bee60>
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/_utils.py", line 797, in _raise
raise ex.with_traceback(sys.exc_info()[2]) # set env var OC_CAUSE=1 for full trace
│ │ │ └
│ │ └ <module 'sys' (built-in)>
│ └ <method 'with_traceback' of 'BaseException' objects>
└ ConfigAttributeError('Missing key length_aware\n full_key: model.model_config.length_aware\n object_type=dict')
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/dictconfig.py", line 351, in getattr
return self._get_impl(
│ └ <function DictConfig._get_impl at 0x738f957ee3b0>
└ {'max_seq_len': 1536, 'model_name': '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/models/MFR/un...
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/dictconfig.py", line 442, in _get_impl
node = self._get_child(
│ └ <function BaseContainer._get_child at 0x738f957d29e0>
└ {'max_seq_len': 1536, 'model_name': '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/models/MFR/un...
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/basecontainer.py", line 73, in _get_child
child = self._get_node(
│ └ <function DictConfig._get_node at 0x738f957ee4d0>
└ {'max_seq_len': 1536, 'model_name': '/home/lh1121871443/.cache/modelscope/hub/opendatalab/PDF-Extract-Kit-1___0/models/MFR/un...
File "/home/lh1121871443/anaconda3/envs/MinerU/lib/python3.10/site-packages/omegaconf/dictconfig.py", line 480, in _get_node
raise ConfigKeyError(f"Missing key {key!s}")
└ <class 'omegaconf.errors.ConfigKeyError'>

omegaconf.errors.ConfigAttributeError: Missing key length_aware
full_key: model.model_config.length_aware
object_type=dict
```

则升级unimernet到0.2.1

如果接着报错，找不到doclayout-yolo，且通过pip无法安装，则手动在pypi.org下载安装: https://pypi.org/project/doclayout-yolo/#files