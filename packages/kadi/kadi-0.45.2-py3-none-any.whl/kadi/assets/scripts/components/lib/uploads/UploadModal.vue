<!-- Copyright 2024 Karlsruhe Institute of Technology
   -
   - Licensed under the Apache License, Version 2.0 (the "License");
   - you may not use this file except in compliance with the License.
   - You may obtain a copy of the License at
   -
   -     http://www.apache.org/licenses/LICENSE-2.0
   -
   - Unless required by applicable law or agreed to in writing, software
   - distributed under the License is distributed on an "AS IS" BASIS,
   - WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   - See the License for the specific language governing permissions and
   - limitations under the License. -->

<template>
  <div class="modal" tabindex="-1" @keydown.enter="handleEnter" ref="modal">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body" ref="modalText"></div>
        <div class="modal-footer justify-content-between">
          <div>
            <button type="button" class="btn btn-sm btn-primary btn-modal" data-dismiss="modal" ref="btnReplace">
              {{ $t('Yes') }}
            </button>
            <button type="button" class="btn btn-sm btn-light btn-modal" data-dismiss="modal" ref="btnCancel">
              {{ $t('No') }}
            </button>
          </div>
          <div class="form-check" v-if="showCheckbox">
            <input type="checkbox" class="form-check-input" :id="`apply-all-${suffix}`" v-model="applyAll">
            <label class="form-check-label" :for="`apply-all-${suffix}`">{{ $t('Apply to all') }}</label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.btn-modal {
  width: 100px;
}
</style>

<script>
export default {
  data() {
    return {
      suffix: kadi.utils.randomAlnum(),
      applyAll: false,
    };
  },
  props: {
    showCheckbox: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    handleEnter() {
      this.$refs.btnReplace.click();
    },
    open(filename) {
      const replaceMsg = $t(
        'A file with the name "{{filename}}" already exists in the current record. Do you want to replace it?',
        {filename},
      );

      return new Promise((resolve) => {
        $(this.$refs.modal).modal({backdrop: 'static', keyboard: false});
        this.$refs.modalText.innerText = replaceMsg;

        let replaceFileHandler = null;
        let cancelUploadHandler = null;

        // Make sure that the event listeners are removed again and the checkbox is reset after resolving the promise by
        // closing the modal via one of the buttons.
        const resolveDialog = (status) => {
          resolve({status, applyAll: this.applyAll});
          this.applyAll = false;
          this.$refs.btnReplace.removeEventListener('click', replaceFileHandler);
          this.$refs.btnCancel.removeEventListener('click', cancelUploadHandler);
        };

        replaceFileHandler = () => resolveDialog(true);
        cancelUploadHandler = () => resolveDialog(false);

        this.$refs.btnReplace.addEventListener('click', replaceFileHandler);
        this.$refs.btnCancel.addEventListener('click', cancelUploadHandler);
      });
    },
  },
  beforeDestroy() {
    $(this.$refs.modal).modal('dispose');
  },
};
</script>
