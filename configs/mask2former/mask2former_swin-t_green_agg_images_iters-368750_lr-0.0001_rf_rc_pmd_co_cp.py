auto_scale_lr = dict(base_batch_size=16, enable=False)
backbone_embed_multi = dict(decay_mult=0.0, lr_mult=0.1)
backbone_norm_multi = dict(decay_mult=0.0, lr_mult=0.1)
backend_args = None
batch_augments = [
    dict(
        img_pad_value=0,
        mask_pad_value=0,
        pad_mask=True,
        pad_seg=False,
        size=(
            1024,
            1024,
        ),
        type='BatchFixedSizePad'),
]
custom_keys = dict({
    'absolute_pos_embed':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone':
    dict(decay_mult=1.0, lr_mult=0.1),
    'backbone.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.patch_embed.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.0.blocks.0.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.0.blocks.1.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.0.downsample.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.1.blocks.0.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.1.blocks.1.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.1.downsample.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.2.blocks.0.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.2.blocks.1.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.2.blocks.2.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.2.blocks.3.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.2.blocks.4.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.2.blocks.5.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.2.downsample.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.3.blocks.0.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'backbone.stages.3.blocks.1.norm':
    dict(decay_mult=0.0, lr_mult=0.1),
    'level_embed':
    dict(decay_mult=0.0, lr_mult=1.0),
    'query_embed':
    dict(decay_mult=0.0, lr_mult=1.0),
    'query_feat':
    dict(decay_mult=0.0, lr_mult=1.0),
    'relative_position_bias_table':
    dict(decay_mult=0.0, lr_mult=0.1)
})
data_preprocessor = dict(
    batch_augments=[
        dict(
            img_pad_value=0,
            mask_pad_value=0,
            pad_mask=True,
            pad_seg=False,
            size=(
                1024,
                1024,
            ),
            type='BatchFixedSizePad'),
    ],
    bgr_to_rgb=True,
    mask_pad_value=0,
    mean=[
        123.675,
        116.28,
        103.53,
    ],
    pad_mask=True,
    pad_seg=False,
    pad_size_divisor=32,
    seg_pad_value=255,
    std=[
        58.395,
        57.12,
        57.375,
    ],
    type='DetDataPreprocessor')
data_root = '/mt/sdb/TrainCell/green_agg_inseg_dataset'
dataset_type = 'CocoDataset'
default_hooks = dict(
    checkpoint=dict(
        by_epoch=False,
        interval=5000,
        max_keep_ckpts=3,
        save_best='auto',
        save_last=True,
        type='CheckpointHook'),
    logger=dict(interval=10, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(type='DetVisualizationHook'))
default_scope = 'mmdet'
depths = [
    2,
    2,
    6,
    2,
]
dynamic_intervals = [
    (
        365001,
        368750,
    ),
]
embed_multi = dict(decay_mult=0.0, lr_mult=1.0)
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
image_size = (
    1024,
    1024,
)
interval = 5000
load_from = 'checkpoints/mask2former_swin-t-p4-w7-224_8xb2-lsj-50e_coco_20220508_091649-01b0f990.pth'
log_level = 'INFO'
log_processor = dict(by_epoch=False, type='LogProcessor', window_size=50)
max_iters = 368750
metainfo = dict(
    classes='green_agg', palette=[
        (
            0,
            255,
            0,
        ),
    ])
model = dict(
    backbone=dict(
        attn_drop_rate=0.0,
        convert_weights=True,
        depths=[
            2,
            2,
            6,
            2,
        ],
        drop_path_rate=0.3,
        drop_rate=0.0,
        embed_dims=96,
        frozen_stages=-1,
        init_cfg=dict(
            checkpoint=
            'https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_tiny_patch4_window7_224.pth',
            type='Pretrained'),
        mlp_ratio=4,
        num_heads=[
            3,
            6,
            12,
            24,
        ],
        out_indices=(
            0,
            1,
            2,
            3,
        ),
        patch_norm=True,
        qk_scale=None,
        qkv_bias=True,
        type='SwinTransformer',
        window_size=7,
        with_cp=False),
    data_preprocessor=dict(
        batch_augments=[
            dict(
                img_pad_value=0,
                mask_pad_value=0,
                pad_mask=True,
                pad_seg=False,
                size=(
                    1024,
                    1024,
                ),
                type='BatchFixedSizePad'),
        ],
        bgr_to_rgb=True,
        mask_pad_value=0,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        pad_mask=True,
        pad_seg=False,
        pad_size_divisor=32,
        seg_pad_value=255,
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type='DetDataPreprocessor'),
    init_cfg=None,
    panoptic_fusion_head=dict(
        init_cfg=None,
        loss_panoptic=None,
        num_stuff_classes=0,
        num_things_classes=1,
        type='MaskFormerFusionHead'),
    panoptic_head=dict(
        enforce_decoder_input_project=False,
        feat_channels=256,
        in_channels=[
            96,
            192,
            384,
            768,
        ],
        loss_cls=dict(
            class_weight=[
                1.0,
                0.1,
            ],
            loss_weight=2.0,
            reduction='mean',
            type='CrossEntropyLoss',
            use_sigmoid=False),
        loss_dice=dict(
            activate=True,
            eps=1.0,
            loss_weight=5.0,
            naive_dice=True,
            reduction='mean',
            type='DiceLoss',
            use_sigmoid=True),
        loss_mask=dict(
            loss_weight=5.0,
            reduction='mean',
            type='CrossEntropyLoss',
            use_sigmoid=True),
        num_queries=100,
        num_stuff_classes=0,
        num_things_classes=1,
        num_transformer_feat_level=3,
        out_channels=256,
        pixel_decoder=dict(
            act_cfg=dict(type='ReLU'),
            encoder=dict(
                layer_cfg=dict(
                    ffn_cfg=dict(
                        act_cfg=dict(inplace=True, type='ReLU'),
                        embed_dims=256,
                        feedforward_channels=1024,
                        ffn_drop=0.0,
                        num_fcs=2),
                    self_attn_cfg=dict(
                        batch_first=True,
                        dropout=0.0,
                        embed_dims=256,
                        num_heads=8,
                        num_levels=3,
                        num_points=4)),
                num_layers=6),
            norm_cfg=dict(num_groups=32, type='GN'),
            num_outs=3,
            positional_encoding=dict(normalize=True, num_feats=128),
            type='MSDeformAttnPixelDecoder'),
        positional_encoding=dict(normalize=True, num_feats=128),
        strides=[
            4,
            8,
            16,
            32,
        ],
        transformer_decoder=dict(
            init_cfg=None,
            layer_cfg=dict(
                cross_attn_cfg=dict(
                    batch_first=True, dropout=0.0, embed_dims=256,
                    num_heads=8),
                ffn_cfg=dict(
                    act_cfg=dict(inplace=True, type='ReLU'),
                    embed_dims=256,
                    feedforward_channels=2048,
                    ffn_drop=0.0,
                    num_fcs=2),
                self_attn_cfg=dict(
                    batch_first=True, dropout=0.0, embed_dims=256,
                    num_heads=8)),
            num_layers=9,
            return_intermediate=True),
        type='Mask2FormerHead'),
    test_cfg=dict(
        filter_low_score=True,
        instance_on=True,
        iou_thr=0.8,
        max_per_image=75,
        panoptic_on=False,
        semantic_on=False),
    train_cfg=dict(
        assigner=dict(
            match_costs=[
                dict(type='ClassificationCost', weight=2.0),
                dict(
                    type='CrossEntropyLossCost', use_sigmoid=True, weight=5.0),
                dict(eps=1.0, pred_act=True, type='DiceCost', weight=5.0),
            ],
            type='HungarianAssigner'),
        importance_sample_ratio=0.75,
        num_points=12544,
        oversample_ratio=3.0,
        sampler=dict(type='MaskPseudoSampler')),
    type='Mask2Former')
num_classes = 1
num_stuff_classes = 0
num_things_classes = 1
optim_wrapper = dict(
    clip_grad=dict(max_norm=0.01, norm_type=2),
    optimizer=dict(
        betas=(
            0.9,
            0.999,
        ),
        eps=1e-08,
        lr=0.0001,
        type='AdamW',
        weight_decay=0.05),
    paramwise_cfg=dict(
        custom_keys=dict({
            'absolute_pos_embed':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone':
            dict(decay_mult=1.0, lr_mult=0.1),
            'backbone.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.patch_embed.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.0.blocks.0.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.0.blocks.1.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.0.downsample.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.1.blocks.0.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.1.blocks.1.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.1.downsample.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.2.blocks.0.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.2.blocks.1.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.2.blocks.2.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.2.blocks.3.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.2.blocks.4.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.2.blocks.5.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.2.downsample.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.3.blocks.0.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'backbone.stages.3.blocks.1.norm':
            dict(decay_mult=0.0, lr_mult=0.1),
            'level_embed':
            dict(decay_mult=0.0, lr_mult=1.0),
            'query_embed':
            dict(decay_mult=0.0, lr_mult=1.0),
            'query_feat':
            dict(decay_mult=0.0, lr_mult=1.0),
            'relative_position_bias_table':
            dict(decay_mult=0.0, lr_mult=0.1)
        }),
        norm_decay_mult=0.0),
    type='OptimWrapper')
param_scheduler = dict(
    begin=0,
    by_epoch=False,
    end=368750,
    gamma=0.1,
    milestones=[
        327778,
        355092,
    ],
    type='MultiStepLR')
pretrained = 'https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_tiny_patch4_window7_224.pth'
resume = False
test_cfg = dict(type='TestLoop')
test_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='val/annotation_coco.json',
        backend_args=None,
        data_prefix=dict(img='val/', seg='annotations/panoptic_val2017/'),
        data_root='/mt/sdb/TrainCell/green_agg_inseg_dataset',
        metainfo=dict(classes='green_agg', palette=[
            (
                0,
                255,
                0,
            ),
        ]),
        pipeline=[
            dict(backend_args=None, to_float32=True, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    ann_file=
    '/mt/sdb/TrainCell/green_agg_inseg_dataset/val/annotation_coco.json',
    backend_args=None,
    format_only=False,
    metric=[
        'bbox',
        'segm',
    ],
    type='CocoMetric')
test_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(keep_ratio=False, scale=(
        1024,
        1024,
    ), type='Resize'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(
        meta_keys=(
            'img_id',
            'img_path',
            'ori_shape',
            'img_shape',
            'scale_factor',
        ),
        type='PackDetInputs'),
]
train_cfg = dict(
    dynamic_intervals=[
        (
            365001,
            368750,
        ),
    ],
    max_iters=368750,
    type='IterBasedTrainLoop',
    val_interval=100)
train_dataloader = dict(
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    batch_size=1,
    dataset=dict(
        ann_file='train/annotation_coco.json',
        backend_args=None,
        data_prefix=dict(img='train/', seg='annotations/panoptic_train2017/'),
        data_root='/mt/sdb/TrainCell/green_agg_inseg_dataset',
        filter_cfg=dict(filter_empty_gt=True, min_size=32),
        metainfo=dict(classes='green_agg', palette=[
            (
                0,
                255,
                0,
            ),
        ]),
        pipeline=[
            dict(backend_args=None, to_float32=True, type='LoadImageFromFile'),
            dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
            dict(prob=0.5, type='RandomFlip'),
            dict(
                keep_ratio=True,
                ratio_range=(
                    0.1,
                    2.0,
                ),
                resize_type='Resize',
                scale=(
                    1024,
                    1024,
                ),
                type='RandomResize'),
            dict(
                allow_negative_crop=True,
                crop_size=(
                    1024,
                    1024,
                ),
                crop_type='absolute',
                recompute_bbox=True,
                type='RandomCrop'),
            dict(
                by_mask=True,
                min_gt_bbox_wh=(
                    1e-05,
                    1e-05,
                ),
                type='FilterAnnotations'),
            dict(type='PackDetInputs'),
        ],
        type='CocoDataset'),
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(
        poly2mask=False,
        type='LoadAnnotations',
        with_bbox=True,
        with_mask=True),
    dict(keep_ratio=False, scales=(
        1024,
        1024,
    ), type='RandomChoiceResize'),
    dict(direction=[
        'horizontal',
        'vertical',
    ], prob=0.5, type='RandomFlip'),
    dict(
        crop_size=(
            0.5,
            0.5,
        ), crop_type='relative_range', type='RandomCrop'),
    dict(
        brightness_delta=32,
        contrast_range=(
            0.5,
            1.5,
        ),
        hue_delta=18,
        saturation_range=(
            0.5,
            1.5,
        ),
        type='PhotoMetricDistortion'),
    dict(
        cutout_shape=[
            (
                16,
                16,
            ),
            (
                32,
                32,
            ),
        ],
        fill_in=(
            0,
            0,
        ),
        n_holes=(
            0,
            20,
        ),
        p=0.5,
        type='CutOut'),
    dict(
        bbox_occluded_thr=10,
        mask_occluded_thr=300,
        max_num_pasted=10,
        p=0.5,
        paste_by_box=False,
        selected=True,
        type='CopyPaste'),
    dict(type='PackDetInputs'),
]
val_cfg = dict(type='ValLoop')
val_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='val/annotation_coco.json',
        backend_args=None,
        data_prefix=dict(img='val/', seg='annotations/panoptic_val2017/'),
        data_root='/mt/sdb/TrainCell/green_agg_inseg_dataset',
        metainfo=dict(classes='green_agg', palette=[
            (
                0,
                255,
                0,
            ),
        ]),
        pipeline=[
            dict(backend_args=None, to_float32=True, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    ann_file=
    '/mt/sdb/TrainCell/green_agg_inseg_dataset/val/annotation_coco.json',
    backend_args=None,
    format_only=False,
    metric=[
        'segm',
    ],
    type='CocoMetric')
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='DetLocalVisualizer',
    vis_backends=[
        dict(
            save_dir=
            '/mt/sdb/TrainCell/work_dirs/green_agg_images_exps_v1/mask2former_swin-t_green_agg_images_iters-368750_lr-0.0001_rf_rc_pmd_co_cp',
            type='LocalVisBackend'),
        dict(type='TensorboardVisBackend'),
        dict(
            init_kwargs=dict(
                group='mask2former_swin-t',
                name=
                'mask2former_swin-t_green_agg_images_iters-368750_lr-0.0001_rf_rc_pmd_co_cp',
                project='green_agg_images_exps_v1'),
            type='WandbVisBackend'),
    ])
work_dir = '/mt/sdb/TrainCell/work_dirs/green_agg_images_exps_v1/mask2former_swin-t_green_agg_images_iters-368750_lr-0.0001_rf_rc_pmd_co_cp'
